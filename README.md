# dataset-person-name-disambiguation
creating a dataset for person name disambiguation using combination of sources like wikipedia, DBLP authors and PPDB.

## Download various sources

### 1. DBPedia [ref](http://wiki.dbpedia.org/services-resources/datasets/previous-releases/data-set-36)
```
wget http://downloads.dbpedia.org/3.6/en/persondata_en.nt.bz2
bzip2 -d persondata_en.nt.bz2
wget http://downloads.dbpedia.org/3.6/en/disambiguations_en.nt.bz2
bzip2 -d disambiguations_en.nt.bz2
```

### 2. The Paraphrase Database [ref](http://www.cis.upenn.edu/~ccb/ppdb/)
```
wget http://www.cis.upenn.edu/~ccb/ppdb/release-1.0/ppdb-1.0-s-lexical.gz
gunzip ppdb-1.0-s-lexical.gz
wget http://www.cis.upenn.edu/~ccb/ppdb/release-1.0/ppdb-1.0-s-o2m.gz
gunzip ppdb-1.0-s-o2m.gz
```

### 3. DBLP authors [ref](https://hpi.de/naumann/projects/repeatability/datasets/wpsd.html)
```
wget https://hpi.de/fileadmin/user_upload/fachgebiete/naumann/projekte/repeatability/DBLP/DBLP10k.csv
```

# Dataset Generation

**Step 1 :** run attached createdata.py on downloaded files.
```
python createdata.py > persons.match

```

**Step 2 (optional):** append nnp dataset from ppdb (not necessarily person names but it help in learning spelling patterns)
```
cat ppdb*|grep "\[NNP\]"|awk -F"[|]*[ ]*" '{if($3!=$5 && substr($3,0,1)==substr($5,0,1))print $3"\t"$5"\ty"}' > nnp.match

cat nnp.match >> persons.match
```

# Dataset Sample

|Name|Disambiguation|isVariation|
|---|---|---|
|Marria G Honnet|Marry Honnet|y|
|Mohammed Fazle Baki|Md. Fazle Baki|y|
|Shensheng Zhang|Shen-sheng Zhang|y|
|James B. D. Joshi|James Joshi|y|
|Thomas A. Down|Thomas Down|y|
|Frank Hung-Fat Leung|Frank H. Leung|y|
|Geoffrey W. Hill|G. W. Hill|y|
|Simon L. Harding|Simon Harding|y|
|Antonio Fernández|Antonio Fernández Anta|y|
|Argyrios Zymnis|Argyris Zymnis|y|
|N. R. Achuthan|Nirmala Achutyan|y|
|Fabrice Muamba|Fabrice Muamba|n|
|Ursula Vaughan Williams|Vaughan Williams|y|
|Henry Earle Vaughan|Henry Earle|y|
|Bernard Lens III|Bernard Lens|y|
|Muthukulam Raghavan Pillai|Raghavan|y|
|James Fisher Robinson|James Fisher|y|
|Jimmy Needles|Needle|y|
|W. E. B. Du Bois|Web|y|
|Sylvester Perry Ryan|Perry Ryan|y|
|James Beaty, Jr.|Beaty|y|
|George Manning McDade|George Manning|y|
|Alejandro Zaffaroni|Zaffaroni|n|
|Ellie Goulding|Ellie Goulding|n|





