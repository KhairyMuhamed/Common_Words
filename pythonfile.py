import string
file1=open('HP Lovecraft’s Beyond the Wall of Sleep.txt','r',errors='ignore')
content1=file1.read()
file2=open('Jane Austin’s Pride and Prejudice.txt','r',errors='ignore')
content2=file2.read()
Lcontent1=content1.lower()
Lcontent2=content2.lower()
noPun1=Lcontent1.translate(str.maketrans('', '', string.punctuation))
noPun2=Lcontent2.translate(str.maketrans('', '', string.punctuation))
F1=set(noPun1.split())
F2=set(noPun2.split())
common={'i', 'you', 'he', 'she', 'it', 'we', 'they','me','mine', 'yours', 'his', 'hers', 'ours','their','there','here', 'theirs',
'which', 'who','what','when','while', 'that','this', 'these', 'those','is','are','was','were','after', 'before', 'in','on','at','of','from','a','the',
'us','an','its',',','.','$','&','#',';',':','.','meâ€','"','Ã¢â‚¬',"'",'/','+','-','!','?','22','â€œi','Ã¢â‚¬Å“he','Ã¢â‚¬Å“i','Ã¢â‚¬Å“on','my','myself','meÃ¢â‚¬','your','yourself'}
intersect=(F1.intersection(F2))-common
print(len(intersect))
print(intersect)