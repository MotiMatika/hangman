                #התכנית מקבלת תו מהמשתמש ומודיעה אם התו נמצא או לא נמצא
#txt = "abcdef"                              #השמת מחרוזת קבועה 
#x=input("Guess a letter ")                  # קלט-ניחוש האות ע"י המשתמש
#if x in txt:                                #בדיקה האם התו נמצא במחרוזת הקבועה
#	print("great",x," is in the word")      #פלט-אמת,אם התו נמצא
#else:                                       # אם התו לא נמצא... מ
#	print("sorry",x," isn't in the word")   #פלט- התו לא נמצא

#התכנית מקבלת מילה ומדפיסה את אורכה ע"י קו תחתון כמספר האותיות
txt = input("enter a word :")
length =len(txt) 
print("the lengtf of the word you chose is :",length," letters")
print("_ "*length)


	
#                               #התכנית מבקשת להקליד אות אחת ובודקת אם המשתמש אכן ביצע, ואם לא - מודיעה לו 
# txt=input("type only letters : ")           #הקלדת מילה
# length = len(txt)                           #השמת ערך אורך המילה לתא לנגט
# only_alpha = txt.isalpha()                  #בדיקה אם המחרוזת מכילה רק אותיות ומחזירה כן/לא לתא אונלי-אלפא
# if length > 1 and only_alpha==False:        #בדיקה אם המחרוזת ארוכה מאות אחת וגם לא אותיות         
# 	print("E3")                             #פלט-אי3
# elif length > 1:                            #בדיקה אם אורך המילה גדול מ1
# 	print("E1")                             # פלט - אי1
# elif  only_alpha ==False:                   #בדיקה אם בקלט יש סימן שאינו אות                                       
# 	print("E2")                             # פלט - אי2                   
# else:                                       #אחרת
# 	print(txt.lower())	                    #פלט - אות קטנה בכל מקרה
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#

#txt=input("type only letters : ")                 #קלט
#y=txt.isalpha()                                   #הבדיקה אם במחרוזת יש רק אותיות , והתשובה כן/לא נכנסת לתא ואיי
#if y==True:                                       #השוואה אם בתא ואיי יש אמת - כלומר שיש רק אותיות
#	print("you did well !!!")                     #פלט אם אמת
#else:                                             #אחרת
#	print("Sorry,you didn't type only letters")   #פלט אם יש תו שאינו אות