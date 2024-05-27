#!/bin/bash

CHAPTER=$(printf "%02d" "$1")

echo CHAPTER = $CHAPTER


mkdir -p ./Chapters/Chapter$CHAPTER/RawPages
cd ./Chapters/Chapter$CHAPTER/RawPages
cp /tmp/misc/Italian_By_The_Natural_Method_Chapters/Chapter$CHAPTER.pdf .
gs -sDEVICE=jpeg -r100 -o Chapter$CHAPTER-%03d.jpg ./Chapter$CHAPTER.pdf

cp ../../../scripts/evenpage_master_nointer.svg evenpage.svg
cp ../../../scripts/oddpage_master_nointer.svg oddpage.svg

for file in *.jpg; do
   python3 ../../../scripts/svgmask.py $file
done


inkscape Chapter*.svg


for file in Chapter*.svg; do
    echo "Export maintext001 in $file"
    inkscape --export-type="png" --export-dpi=300 --export-id="maintext001" $file
done

for file in *maintext001.png; do
    echo OCR file $file
    tesseract -l ita $file $file.txt txt pdf
done

ls *.txt | sort -n | awk '1==1 {printf("cat %s\n",$0);}' | cat | sh >../Chapter$CHAPTER-pass01.txt

while true; do
    read -p "Enter Y to continue or N to exit: " user_input
    case $user_input in
        [Yy]* )
            echo "You entered Y. Continuing the script..."
            break
            ;;
        [Nn]* )
            echo "You entered N. Exiting the script..."
            exit 0
            ;;
        * )
            echo "Invalid input. Please enter Y or N."
            ;;
    esac
done

echo "Now create the rest of the files."
