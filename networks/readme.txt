Offences dictionary file

Download and edit the file offence_list.py so that the pathname of the pickle file it creates is something helpful.
Run the file offence_list.py 

Use pickle to import the offences dictionary, choose French (original) or English (mangled) version

> import pickle
> offences = pickle.load(open("C:/Users/rmeek/OneDrive/Documents/mit_analytics/data/networks/Cooffending/offences.pkl", "rb" ) )
> offences = offences["en"]

The dictionary's keys are offence codes, the values are descriptions.

Thanks to benzgeg (https://courses.edx.org/courses/course-v1:MITx+6.419x+1T2021/discussion/forum/users/15146370) for his help with translations, any mistakes that remain are due to my misreadings of https://laws-lois.justice.gc.ca/pdf/c-46.pdf
