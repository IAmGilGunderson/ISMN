# ISMN

L'Italiano secondo il Metodo Natura

This repo is to create well structured data from the book.

The problems are:

The first few chapters have interleaved text with a non IPA pronunciation.

The rest of the book uses diacritic marks to indicate stress which makes the
word appear to be non-standard to dictionary lookup apps.

The marginalia make OCR difficult. It must be removed before OCR.


## Method

mkdir -p ./Chapters/Chapter01/RawPages
cd ./Chapters/Chapter01/RawPages
gs -sDEVICE=jpeg -r100 -o Chapter01-%03d.jpg ./Chapter01.pdf

cp ../../../scripts/evenpage_master.svg evenpage.svg ; cp ../../../scripts/oddpage_master.svg oddpage.svg
or
cp ../../../scripts/evenpage_master_nointer.svg evenpage.svg ; cp ../../../scripts/oddpage_master_nointer.svg oddpage.svg


ls *.jpg | awk '1==1 {printf("python3 ../../../scripts/svgmask.py ./%s\n",$0);}' | sh

inkscape *-even.svg *-odd.svg
or
inkscape Chapter*.svg


echo ### Even and Odd maintext001
ls *-odd.svg | awk '1==1 {printf("inkscape --export-type=\"png\" --export-dpi=300 --export-id=\"maintext001\" ./%s\n",$0);}' | sh
ls *-even.svg | awk '1==1 {printf("inkscape --export-type=\"png\" --export-dpi=300 --export-id=\"maintext001\" ./%s\n",$0);}' | sh
or
ls Chapter*.svg | grep -v "bigimage" | awk '1==1 {printf("inkscape --export-type=\"png\" --export-dpi=300 --export-id=\"maintext001\" ./%s\n",$0);} | sh

echo ### Even and Odd sidebar001
ls *-odd.svg | awk '1==1 {printf("inkscape --export-type=\"png\" --export-dpi=300 --export-id=\"sidebar001\" ./%s\n",$0);}' | sh
ls *-even.svg | awk '1==1 {printf("inkscape --export-type=\"png\" --export-dpi=300 --export-id=\"sidebar001\" ./%s\n",$0);}' | sh
or
ls Chapter*.svg |grep -v "bigimage" | awk '1==1 {printf("inkscape --export-type=\"png\" --export-dpi=300 --export-id=\"sidebar001\" ./%s\n",$0);}' | sh



echo ### the big image
ls *-bigimage.svg | awk '1==1 {printf("inkscape --export-type=\"png\" --export-dpi=300 --export-id=\"bigimage001\" ./%s\n",$0);}' | sh


echo ### Run tesseract-ocr
ls ./*maintext001.png | gawk '1==1 {printf("tesseract -l ita %s %s.txt txt pdf \n",$0,$0);}' | xjobs -j5

echo ### Concatenate all the text files
ls *.txt | sort -n | awk '1==1 {printf("cat %s\n",$0);}' | cat | sh >../Chapter01-pass01.txt

echo # cleanup
rm *.pdf
rename 's/.jpg_maintext001.png.txt//g' *maintext001*
rename 's/.jpg_maintext001/-maintext/g' *maintext*
rename 's/.jpg_sidebar001/-sidebar/g' *sidebar*

#rename 's/.jpg-even_maintext001.png.txt.txt/.txt/g' *.txt
#rename 's/.jpg-odd_maintext001.png.txt.txt/.txt/g' *.txt
#rename -n 's/.jpg-even_sidebar001.png/-sidebar.png/g' *sidebar001.png
#rename  's/.jpg-odd_sidebar001.png/-sidebar.png/g' *sidebar001.png
#rename 's/.jpg-bigimage_bigimage001.png/-bigimage.png/g' *bigimage001.png
#rename -n 's/jpg.txt.txt/txt/g' *.txt


# Passes
Ignore EXERCISES

## Pass01 = just the text as it came from ocr

## Pass02 = remove hyphenations, remove unused diacritics
find -\n
turn on spell check and fix any words that are not real words in the dictionary
  this catches most of the errant diacritics
replace ’ with '

## Pass03 = remove pagination and line breaks to make normal paragraphs
replace \n\n with @@@@
replace \n with _ (space character)
replace @@@@ with \n\n


# Ideas



# make a square that covers the maintext and call it maintext001
# make a square that covers sidebard and call it sidebar001
inkscape --export-type="png" --export-dpi=300 --export-id="maintext001" ./drawing.svg

if page is even then pythonitup.py evenpage.svg replacing @@@@@@@ with ../img.jpeg
then do export of maintext001 sidebar001 bigimage001
ISMN-Chapter0x-Page00x-odd.svg
ISMN-Chapter00-Page00x-even.svg
ISMN-Chapter00-Page00x-bigimage.svg
should create
    ISMN-Chapter00-Page000-maintext.jpg
    ISMN-Chapter00-Page000-sidebar.jpg
    ISMN-Chapter00-Page000-bigimage.jpg # if found

we can use the oddpage_master.svg
               evenpage_master.svg
or can use a chapter by chapter one


