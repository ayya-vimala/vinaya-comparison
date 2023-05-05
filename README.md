# Comparing known Vinaya texts from all schools

The spreadsheet `vinaya_parallels` in vinaya_output is the main file in this repo. The other files in vinaya_output are the raw data which are combined in this file.

The spreadsheet `vinaya_parallels_color` in vinaya_output shows the same data for only the Bhikkhunī Pāṭimokkhas but with a color coding to show which rules have very few parallels.

These spreadsheetw shows the raw dump of the parallels of the Bhikkhu and Bhikkhunī Pāṭimokkhas in all the Buddhist schools, using an API call to the SuttaCentral server for each rule.

## Abbreviations
Some explanation is needed of what you are actually looking at so let’s start by the abbreviations.

Note that for some schools and texts we do not have the data. That does not mean they don’t exist, only that our data is incomplete. 
Like for instance the Bhikkhunī Pāṭimokkha of the Mahāsaṁghika school in Sanskrit. We do however have the Chinese version.
Also the parallels with the Khandhakas are not always complete.

*Tabnames and filenames are formatted as follows: language - school - bhikkhunī or bhikkhu - textname - rule class – number*

These numbers correspond with the actual files in SuttaCentral **

### Languages
* pli  Pali
* lzh  Chinese
* san  Sanskrit
* pgd  Prakrit
* xct  Tibetan

### Schools	
* tv    Theravāda
* mg    Mahāsaṁghika
* lo    Lokuttaravāda
* mi    Mahīśāsaka
* dg    Dharmaguptaka
* sarv  Sarvāstivāda
* mu    Mūlasarvāstivāda

Next to these schools a few texts from the Bhikkhu Pāṭimokkha of other schools are mentioned like Kāśyapīya, Upāliparipṛcchā, Qizil and an other unknown school.
In some cases some extra information is added on a version of a text if multiple versions exist, like for instance ‘tf44’ or ‘finot’.

### Bhikkhunī or Bhikkhu	
* bi	Bhikkhunī
* bu	Bhikkhu

### Textname	
* pm	Pāṭimokkha
* vb	Vibhaṅga
* kd	Khandhaka

### Rule class	
* pj	Pārājika
* ss	Saṅghādisesa
* ay	Aniyata
* np	Nissaggiya Pācittiya
* pc	Pācittiya
* pd	Pāṭidesanīya
* sk	Sekhiya
* as	Adhikaraṇasamatha

** For instance in the first spreadsheet is called pli-tv-bi-pm. This means the Pali Theravāda Bhikkhunī Pāṭimokkha.

The first column mentions this and is marked as pli-tv-bi. Underneath you see in the first row: pm-pj1; vb-pj1
This means Pāṭimokkha Pārājika 1 and Vibhaṅga Pārājika 1

This translates as a link to SuttaCentral as: https://suttacentral.net/pli-tv-bu-pm-pj1 or https://suttacentral.net/pli-tv-bu-vb-pj1 to see the full text of the Vibhaṅga
As the Pāṭimokkha is a list in one file, if you want to see that simply omit the -pj1 from the link to make https://suttacentral.net/pli-tv-bu-pm

## Organisation within tabs

The various tabs in the spreadsheet each take a base Pāṭimokkha which is then compared with the other texts and parallels in the canon. This base Pāṭimokkha is shown in the first column.
Not all Pāṭimokkhas have a tab, only the major ones for which we have a larger amount of data available. Pāṭimokkha fragments of the various schools do not have their own tab for comparison.

## Other files

The files in the folder 'vinaya' are listings of the various texts and rules that we have available.

The spreadsheet `extra_parallels` are parallels I added by hand as they were not in the SuttaCentral data.