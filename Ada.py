from tkinter import *
from tkinter import messagebox
import random
'''
This is a program created as an attempt to provide a safer communication channel between peers.
It has 3 different alphabets that can encrypt a message, they change randomly and so do the pieces of the alphabets, thus making 
the encryption system presumably hard to decipher.
Python 3
Guadalajara, Jalisco, México
3/17/21
Alan Bravo, 15
'''
#Root
Root=Tk()
Root.resizable(0,0)
Root.title("Ada")
Root.config(bd=5)
Root.config(relief="groove")
Root.config(cursor="hand2")

#Frame
Frame1=Frame(width=400,height=280)
Frame1.pack()
Frame1.config(bg="silver")

#Title
Title=Label(Frame1,text="Welcome to Ada")
Title.place(x=125,y=50)
Title.config(font=(15))

#PassLabel
LabelPass=Label(Frame1,text="Password")
LabelPass.place(x=95,y=110)
LabelPass.config(font=("Arial",12))

#PasswordEntry
PassVar=StringVar()
EntryPass=Entry(Frame1,textvariable=PassVar)
EntryPass.place(x=175,y=113)
EntryPass.config(show="*")

#ButtonSend
def SendFunction():
	if PassVar.get()=="112358":
		Frame1.destroy()
		###################################################
		Frame2=Frame(Root,width=700,height=480)
		Frame2.pack()
		Frame2.config(bg="grey")
		Frame2.config(cursor="hand2")

		#Title
		Title=Label(Frame2,text="Encryptor")
		Title.config(font=("Arial",16))
		Title.place(x=305,y=10)
		#Text
		Text1=Text(Frame2)
		Text1.config(width=62,height=8)
		Text1.place(x=100,y=60)

		Text2=Text(Frame2)
		Text2.config(width=62,height=8)
		Text2.place(x=100,y=270)

		ScrollVert1=Scrollbar(Frame2,command=Text1.yview)
		ScrollVert1.place(x=605,y=100)
		Text1.config(yscrollcommand=ScrollVert1.set)

		ScrollVert2=Scrollbar(Frame2,command=Text2.yview)
		ScrollVert2.place(x=605,y=310)
		Text2.config(yscrollcommand=ScrollVert2.set)


		#ExitButton
		def ExitFunction2():
			Question2=messagebox.askquestion("Exit","Would you like to quit the program?")
			if Question2=="yes":
				Root.destroy()
		ExitButton2=Button(Frame2,text="Exit",command=ExitFunction2)
		ExitButton2.place(x=15,y=10)

		#HelpButton
		def HelpFunction():
			messagebox.showinfo("Help",'''To encrypt a message enter the text in the top square and click on the button that reads "Encrypt".	On the other hand if you want to decrypt a message instead of clicking on the button "Encrypt" click on the button "Decrypt". Your message should appear below.
Note 1: Make sure your message has more than 1 character or else it will not be either encrypted or decrypted.
Note 2: Avoid using Enter when encrypting and keep in mind that currently only English and Spanish are fully functioning.

Made by Alan Bravo on 3/17/21''')
		HelpButton=Button(Frame2,text="Help",command=HelpFunction)
		HelpButton.place(x=640,y=10)

		#EncryptButton
		KeyVarAlph=""
		def EncryptFunction():
			'''
			Alphabet1=[aaabcdeefghiijklmnñooopqrrssstuuvwxyz!?¿¡.,          áéíóú:;12344567890ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ%'$(@)] KeysE=☼,♂,♫ KeysB=‡,☓,⋆ KeysM=☩,♆,ℯ
			Alphabet1=[!×õntqeç#avjåñ<ro¡*4ø©sw6î_¶ÝdyÄx)p1f¿°%(b=7½∩≥≤░▒ε≡⌡0923&$Θclug→hkz>;-´Y{¬+UT^RQPOÑNM}KJIH¨FEDCBAÉÁÍÚÓ|▌▄♦@↕] 

			Alphabet2=[aaabbccddeeffgghhiijjkkllmmmnnñooppqqrrssttuuvvwwxxxyyzz!!??¿¿¡¡...,,     áéíóú:;11223455678900AABBCCDDEEFFGGHHIIJJKKLLMMÑÑOOPPQQRRSSTTUUVVWWXXYYZZÁÉÍÓÚ%%''$$( )@] Keys=E…,†,³,— KeysB=♯,﹖,ϡ,‽ KeysM=❆,✆,❅,☥
			Alphabet2=[○◄‼ÇÉá░└╨α≡üæí▒┴╤ß±abdc→eFghéÆió▓┬╥jklmnñopqrstuxvΓ≥âôú│├╙π≤äö┤─╘Σ⌠àò╡┼╒σ⌡åûª╢╞╓µ÷8ç≈ù9ºτ╖32╟╫1êEf❞ÿ¿zZ╕╚╪ΦHGAB°èÜ¬C║╩┌Ω·ï¢½╗╦█δ√î£¼╝╠▄∞ⁿì¥¡╜{)═▌φ²Ä«╛╬▐ε■Åƒ»┐✰Ⓐ♬]

			Alphabet3=[ aabcdefghijklmnñopqrstuvwxyz!?¿¡.,          áéíóú:;1234567890ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ÁÉÍÓÚ%'$()@] KeysE=☭▦,✞⊗,✢ᶶ KeysB=⁈ᶽ,✹ᵜ,⁇➻ KeysM1=✑,✫,☻  KeysM2=⚥,❦,◍ KeysM3=℮,✾,⚘ KeysM4=ℓ,र,₢
			Alphabet3=[❅ß±abdcEeFghéÆió▓≕╥jklmn┬ñopqrstuxvΓ≥âô⇫│├╙π≤äö┤─╘Σ⌠àòHGBA°èÜ¬C║╩┌Ω·ï¢½╗╦█╝╠▄∞ⁿì¥¡╜═{▌φ²Ä«╛╬▐ε■ÅYwí]
			'''
			if len(Text1.get("1.0",END))<3:
				messagebox.showwarning("Warning","You cannot encrypt messages with less than 2 characters.")
			else:
				Text2.delete(1.0,END)
				Text2.config(fg="black")
				RandomNumber=random.randint(0,100)##############################################################################
				if 50<=RandomNumber<=75:
					Counter0=0
					MidCounter0=0
					RandomNumberAlph1=random.randint(1,3)
					if RandomNumberAlph1==1 or RandomNumberAlph1==2 or RandomNumberAlph1==3:
						for i in Text1.get("1.0",END):
							while Counter0!=1:
								if RandomNumberAlph1==1:
									Text2.insert(END,"‡")
								elif RandomNumberAlph1==2:
									Text2.insert(END,"☓")
								elif RandomNumberAlph1==3:
									Text2.insert(END,"⋆")
								Counter0=+1

							if len(Text2.get("1.0",END))>300:
								while MidCounter0!=1:
									if RandomNumberAlph1==1:
										Text2.insert(END,"☩")
										MidCounter0=+1
									elif RandomNumberAlph1==2:
										Text2.insert(END,"♆")
										MidCounter0=+1
									elif RandomNumberAlph1==3:
										Text2.insert(END,"ℯ")
										MidCounter0=+1
							if i=="a":
								RandomNumberA=random.randint(1,5)
								if RandomNumberA==1:
									Text2.insert(END,"!∟")
								elif RandomNumberA==2:
									Text2.insert(END,"!")
								elif RandomNumberA==3:
									Text2.insert(END,"∟×")
								elif RandomNumberA==4:
									Text2.insert(END,"×")
								elif RandomNumberA==5:
									Text2.insert(END,"õ")
							if i=="b":
								Text2.insert(END,"÷n○")
							if i=="c":
								Text2.insert(END,"•t")
							if i=="d":
								Text2.insert(END,"÷q£")
							if i=="e":
								NumeroRandom=random.randint(1,3)
								if NumeroRandom==1:
									Text2.insert(END,"§e±")
								elif NumeroRandom==2:
									Text2.insert(END,"e")
								elif NumeroRandom==3:
									Text2.insert(END,"ç")
							if i=="f":
								Text2.insert(END,"#○Ž")
							if i=="g":
								Text2.insert(END,"aΔƒ")
							if i=="h":
								Text2.insert(END,"v‰")
							if i=="i":
								NumeroRandom=random.randint(1,3)
								if NumeroRandom==1:
									Text2.insert(END,"σj")
								elif NumeroRandom==2:
									Text2.insert(END,"jσ")
								elif NumeroRandom==3:
									Text2.insert(END,"å")
							if i=="j":
								Text2.insert(END,"≈ñ")
							if i=="k":
								Text2.insert(END,"<∟")
							if i=="l":
								Text2.insert(END,"r±")
							if i=="m":
								NumeroRandom=random.randint(1,2)
								if NumeroRandom==1:
									Text2.insert(END,"£o")
								elif NumeroRandom==2:
									Text2.insert(END,"o")
							if i=="n":
								Text2.insert(END,"∟¡╘")
							if i=="ñ":
								Text2.insert(END,"*σσ")
							if i=="o":
								NumeroRandom=random.randint(1,3)
								if NumeroRandom==1:
									Text2.insert(END,"4•")
								elif NumeroRandom==2:
									Text2.insert(END,"ø")
								elif NumeroRandom==3:
									Text2.insert(END,"©")
							if i=="p":
								Text2.insert(END,"○s")
							if i=="q":
								Text2.insert(END,"w≈")
							if i=="r":
								NumeroRandom=random.randint(1,3)
								if NumeroRandom==1:
									Text2.insert(END,"Σ6")
								elif NumeroRandom==2:
									Text2.insert(END,"î")
								elif NumeroRandom==3:
									Text2.insert(END,"6Σ")
							if i=="s":
								NumeroRandom=random.randint(1,3)
								if NumeroRandom==1:
									Text2.insert(END,"ß_")
								elif NumeroRandom==2:
									Text2.insert(END,"¶")
								elif NumeroRandom==3:
									Text2.insert(END,"Ý")
							if i=="t":
								Text2.insert(END,"d○÷")
							if i=="u":
								NumeroRandom=random.randint(1,3)
								if NumeroRandom==1:
									Text2.insert(END,"yÆ")
								elif NumeroRandom==2:
									Text2.insert(END,"y")
								elif NumeroRandom==3:
									Text2.insert(END,"Ä")
							if i=="v":
								Text2.insert(END,"x§")
							if i=="w":
								Text2.insert(END,")")
							if i=="x":
								Text2.insert(END,"p£")
							if i=="y":
								Text2.insert(END,"1σ")
							if i=="z":
								Text2.insert(END,"fΔ")
							if i==" ":
								NumeroRandom=random.randint(1,10)
								if NumeroRandom==1:
									Text2.insert(END,"7")
								elif NumeroRandom==2:
									Text2.insert(END,"½")
								elif NumeroRandom==3:
									Text2.insert(END,"∩")
								elif NumeroRandom==4:
									Text2.insert(END,"≥")
								elif NumeroRandom==5:
									Text2.insert(END,"≤")
								elif NumeroRandom==6:
									Text2.insert(END,"░")
								elif NumeroRandom==7:
									Text2.insert(END,"▒")
								elif NumeroRandom==8:
									Text2.insert(END,"ε")
								elif NumeroRandom==9:
									Text2.insert(END,"≡")
								elif NumeroRandom==10:
									Text2.insert(END,"⌡")
							if i=="!":
								Text2.insert(END,"¿ß")
							if i=="?":
								Text2.insert(END,"σ°")
							if i=="¿":
								Text2.insert(END,"%")
							if i=="¡":
								Text2.insert(END,"(ƒ")
							if i==".":
								NumeroRandom=random.randint(1,2)
								if NumeroRandom==1:
									Text2.insert(END,"b")
								elif NumeroRandom==2:
									Text2.insert(END,"σb")
							if i==",":
								Text2.insert(END,"◘=")
							if i=="á":
								Text2.insert(END,"0")
							if i=="é":
								Text2.insert(END,"9φ")
							if i=="í":
								Text2.insert(END,"2")
							if i=="ó":
								Text2.insert(END,"φ3")
							if i=="ú":
								Text2.insert(END,"±&")
							if i==":":
								Text2.insert(END,"$")
							if i=="1":
								Text2.insert(END,"c§")
							if i=="2":
								Text2.insert(END,"ƒl")
							if i=="3":
								Text2.insert(END,"uφ")
							if i=="4":
								NumeroRandom=random.randint(1,3)
								if NumeroRandom==1:
									Text2.insert(END,"g◘")
								elif NumeroRandom==2:
									Text2.insert(END,"g")
								elif NumeroRandom==3:
									Text2.insert(END,"→")
							if i=="5":
								Text2.insert(END,"h")
							if i=="6":
								Text2.insert(END,"φk")
							if i=="7":
								Text2.insert(END,"zΣ")
							if i=="8":
								Text2.insert(END,">•")
							if i=="9":
								Text2.insert(END,";╘")
							if i=="0":
								Text2.insert(END,"-")
							if i=="A":
								NumeroRandom=random.randint(1,3)
								if NumeroRandom==1:
									Text2.insert(END,"Δ´Δ")
								elif NumeroRandom==2:
									Text2.insert(END,"´")
								elif NumeroRandom==3:
									Text2.insert(END,"⌠")
							if i=="B":
								Text2.insert(END,"Y")
							if i=="C":
								Text2.insert(END,"{")
							if i=="D":
								Text2.insert(END,"¬")
							if i=="E":
								Text2.insert(END,"+")
							if i=="F":
								Text2.insert(END,"U")
							if i=="G":
								Text2.insert(END,"T")
							if i=="H":
								Text2.insert(END,"^♠")
							if i=="I":
								Text2.insert(END,"≈R")
							if i=="J":
								Text2.insert(END,"Q÷÷")
							if i=="K":
								Text2.insert(END,"§P")
							if i=="L":
								Text2.insert(END,"O")
							if i=="M":
								Text2.insert(END,"Ñ‰")
							if i=="N":
								Text2.insert(END,"N≈")
							if i=="Ñ":
								Text2.insert(END,"M")
							if i=="O":
								Text2.insert(END,"}")
							if i=="P":
								Text2.insert(END,"K")
							if i=="Q":
								Text2.insert(END,"J╘")
							if i=="R":
								Text2.insert(END,"•I")
							if i=="S":
								Text2.insert(END,"Hƒ")
							if i=="T":
								Text2.insert(END,"¨Ž")
							if i=="U":
								Text2.insert(END,"Fσ")
							if i=="V":
								Text2.insert(END,"ÆE")
							if i=="W":
								Text2.insert(END,"╘D")
							if i=="X":
								Text2.insert(END,"C")
							if i=="Y":
								Text2.insert(END,"ŽB")
							if i=="Z":
								Text2.insert(END,"Aφ")
							if i=="Á":
								Text2.insert(END,"ÉÆ")
							if i=="É":
								Text2.insert(END,"‰A")
							if i=="Í":
								Text2.insert(END,"ÍΔ")
							if i=="Ó":
								Text2.insert(END,"Ú‰")
							if i=="Ú":
								Text2.insert(END,"Ó§")
							if i=="%":
								Text2.insert(END,"|")
							if i=="(":
								Text2.insert(END,"♦")
							if i=="@":
								Text2.insert(END,"@Ž")
							if i==")":
								Text2.insert(END,"↕")
							if i=="'":
								Text2.insert(END,"▌")
							if i=="$":
								Text2.insert(END,"▄")
							if i==";":
								Text2.insert(END,"Θ")
				
						if RandomNumberAlph1==1:
							Text2.insert(END,"☼ⁿ")
						elif RandomNumberAlph1==2:
							Text2.insert(END,"♂")
						elif RandomNumberAlph1==3:
							Text2.insert(END,"♫")


					

				elif 0<=RandomNumber<50:
					RandomNumberAlph2=random.randint(1,4)
					SovietCounter=0
					Counter1=0
					MidCounter=0
					if RandomNumberAlph2==1 or  RandomNumberAlph2==2 or RandomNumberAlph2==3 or  RandomNumberAlph2==4:
						for i in Text1.get("1.0",END):
							if len(Text2.get("1.0",END))>1000:
								Text2.insert(END," ")
							if len(Text2.get("1.0",END))>10000:
								Text2.insert(END,"  ")
							if len(Text2.get("1.0",END))>13000:
								Text2.insert(END,"   ")
							if len(Text2.get("1.0",END))>15000:
								while SovietCounter!=3:
										Text2.insert(END,'''USSR☭''')
										SovietCounter=SovietCounter+1

							while Counter1!=1:
								if RandomNumberAlph2==1:
									Text2.insert(END,"♯")
								elif RandomNumberAlph2==2:
									Text2.insert(END,"ϡ")
								elif RandomNumberAlph2==3:
									Text2.insert(END,"﹖")
								elif RandomNumberAlph2==4:
									Text2.insert(END,"‽")
								Counter1=+1

							if len(Text2.get("1.0",END))>=278:
								while MidCounter!=1:
									if RandomNumberAlph2==1:
										Text2.insert(END,"❆")
										MidCounter=+1
									elif RandomNumberAlph2==2:
										Text2.insert(END,"❅")
										MidCounter=+1
									elif RandomNumberAlph2==3:
										Text2.insert(END,"✆")
										MidCounter=+1
									elif RandomNumberAlph2==4:
										Text2.insert(END,"☥")
										MidCounter=+1


							if i=="a":
								RandomNumbera=random.randint(1,3)
								if RandomNumbera==1:
									Text2.insert(END,"○")
								elif RandomNumbera==2:
									Text2.insert(END,"◄")
								elif RandomNumbera==3:
									Text2.insert(END,"‼")
							if i=="b":
								RandomNumberb=random.randint(1,2)
								if RandomNumberb==1:
									Text2.insert(END,"Ç")
								elif RandomNumberb==2:
									Text2.insert(END,"É")
							if i=="c":
								RandomNumberc=random.randint(1,2)
								if RandomNumberc==1:
									Text2.insert(END,"á")
								elif RandomNumberc==2:
									Text2.insert(END,"░")
							if i=="d":
								RandomNumberd=random.randint(1,2)
								if RandomNumberd==1:
									Text2.insert(END,"└")
								elif RandomNumberd==2:
									Text2.insert(END,"╨")
							if i=="e":
								RandomNumbere=random.randint(1,2)
								if RandomNumbere==1:
									Text2.insert(END,"α")
								elif RandomNumbere==2:
									Text2.insert(END,"≡")
							if i=="f":
								RandomNumberf=random.randint(1,2)
								if RandomNumberf==1:
									Text2.insert(END,"ü")
								elif RandomNumberf==2:
									Text2.insert(END,"æ")
							if i=="g":
								RandomNumberg=random.randint(1,2)
								if RandomNumberg==1:
									Text2.insert(END,"í")
								elif RandomNumberg==2:
									Text2.insert(END,"▒")
							if i=="h":
								RandomNumberh=random.randint(1,2)
								if RandomNumberh==1:
									Text2.insert(END,"┴")
								elif RandomNumberh==2:
									Text2.insert(END,"╤")
							if i=="i":
								RandomNumberi=random.randint(1,2)
								if RandomNumberi==1:
									Text2.insert(END,"ß")
								elif RandomNumberi==2:
									Text2.insert(END,"±")
							if i=="j":
								RandomNumberj=random.randint(1,2)
								if RandomNumberj==1:
									Text2.insert(END,"a")
								elif RandomNumberj==2:
									Text2.insert(END,"b")
							if i=="k":
								RandomNumberk=random.randint(1,2)
								if RandomNumberk==1:
									Text2.insert(END,"d")
								elif RandomNumberk==2:
									Text2.insert(END,"c")
							if i=="l":
								RandomNumberl=random.randint(1,2)
								if RandomNumberl==1:
									Text2.insert(END,"→")
								elif RandomNumberl==2:
									Text2.insert(END,"e")
							if i=="m":
								RandomNumberm=random.randint(1,3)
								if RandomNumberm==1:
									Text2.insert(END,"F")
								elif RandomNumberm==2:
									Text2.insert(END,"g")
								elif RandomNumberm==3:
									Text2.insert(END,"h")
							if i=="n":
								RandomNumbern=random.randint(1,2)
								if RandomNumbern==1:
									Text2.insert(END,"Æ")
								elif RandomNumbern==2:
									Text2.insert(END,"é")
							if i=="ñ":
								Text2.insert(END,"i")
							if i=="o":
								RandomNumbero=random.randint(1,2)
								if RandomNumbero==1:
									Text2.insert(END,"ó")
								elif RandomNumbero==2:
									Text2.insert(END,"▓")
							if i=="p":
								RandomNumberp=random.randint(1,2)
								if RandomNumberp==1:
									Text2.insert(END,"┬")
								elif RandomNumberp==2:
									Text2.insert(END,"╥")
							if i=="q":
								RandomNumberq=random.randint(1,2)
								if RandomNumberq==1:
									Text2.insert(END,"j")
								elif RandomNumberq==2:
									Text2.insert(END,"k")
							if i=="r":
								RandomNumberr=random.randint(1,2)
								if RandomNumberr==1:
									Text2.insert(END,"l")
								elif RandomNumberr==2:
									Text2.insert(END,"m")
							if i=="s":
								RandomNumbers=random.randint(1,2)
								if RandomNumbers==1:
									Text2.insert(END,"n")
								elif RandomNumbers==2:
									Text2.insert(END,"ñ")
							if i=="t":
								RandomNumbert=random.randint(1,2)
								if RandomNumbert==1:
									Text2.insert(END,"o")
								elif RandomNumbert==2:
									Text2.insert(END,"p")
							if i=="u":
								RandomNumberu=random.randint(1,2)
								if RandomNumberu==1:
									Text2.insert(END,"q")
								elif RandomNumberu==2:
									Text2.insert(END,"r")
							if i=="v":
								RandomNumberv=random.randint(1,2)
								if RandomNumberv==1:
									Text2.insert(END,"s")
								elif RandomNumberv==2:
									Text2.insert(END,"t")
							if i=="w":
								RandomNumberw=random.randint(1,2)
								if RandomNumberw==1:
									Text2.insert(END,"u")
								elif RandomNumberw==2:
									Text2.insert(END,"x")
							if i=="x":
								RandomNumberx=random.randint(1,3)
								if RandomNumberx==1:
									Text2.insert(END,"v")
								elif RandomNumberx==2:
									Text2.insert(END,"Γ")
								elif RandomNumberx==3:
									Text2.insert(END,"≥")
							if i=="y":
								RandomNumbery=random.randint(1,2)
								if RandomNumbery==1:
									Text2.insert(END,"â")
								elif RandomNumbery==2:
									Text2.insert(END,"ô")
							if i=="z":
								RandomNumberz=random.randint(1,2)
								if RandomNumberz==1:
									Text2.insert(END,"ú")
								elif RandomNumberz==2:
									Text2.insert(END,"│")
							if i=="!":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"├")
								elif RandomNumber==2:
									Text2.insert(END,"╙")
							if i=="?":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"π")
								elif RandomNumber==2:
									Text2.insert(END,"≤")
							if i=="¿":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"ä")
								elif RandomNumber==2:
									Text2.insert(END,"ö")
							if i=="¡":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"┤")
								elif RandomNumber==2:
									Text2.insert(END,"─")
							if i==".":
								RandomNumber=random.randint(1,3)
								if RandomNumber==1:
									Text2.insert(END,"╘")
								elif RandomNumber==2:
									Text2.insert(END,"Σ")
								elif RandomNumber==3:
									Text2.insert(END,"⌠")
							if i==",":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"à")
								elif RandomNumber==2:
									Text2.insert(END,"ò")
							if i==" ":
								RandomNumber=random.randint(1,5)
								if RandomNumber==1:
									Text2.insert(END,"╡")
								elif RandomNumber==2:
									Text2.insert(END,"┼")
								elif RandomNumber==3:
									Text2.insert(END,"╒")
								elif RandomNumber==4:
									Text2.insert(END,"σ")
								elif RandomNumber==5:
									Text2.insert(END,"⌡")
							if i=="á":
								Text2.insert(END,"å")
							if i=="é":
								Text2.insert(END,"û")
							if i=="í":
								Text2.insert(END,"ª")
							if i=="ó":
								Text2.insert(END,"╢")
							if i=="ú":
								Text2.insert(END,"╞")
							if i==":":
								Text2.insert(END,"╓")
							if i==";":
								Text2.insert(END,"µ")
							if i=="1":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"÷")
								elif RandomNumber==2:
									Text2.insert(END,"8")
							if i=="2":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"ç")
								elif RandomNumber==2:
									Text2.insert(END,"≈")
							if i=="3":
								Text2.insert(END,"ù")
							if i=="4":
								Text2.insert(END,"9")
							if i=="5":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"º")
								elif RandomNumber==2:
									Text2.insert(END,"τ")
							if i=="6":
								Text2.insert(END,"╖")
							if i=="7":
								Text2.insert(END,"3")
							if i=="8":
								Text2.insert(END,"2")
							if i=="9":
								Text2.insert(END,"╟")
							if i=="0":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"╫")
								elif RandomNumber==2:
									Text2.insert(END,"1")
							if i=="A":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"ê")
								elif RandomNumber==2:
									Text2.insert(END,"E")
							if i=="B":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"f")
								elif RandomNumber==2:
									Text2.insert(END,"❞")
							if i=="C":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"ÿ")
								elif RandomNumber==2:
									Text2.insert(END,"¿")
							if i=="D":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"z")
								elif RandomNumber==2:
									Text2.insert(END,"Z")
							if i=="E":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"╕")
								elif RandomNumber==2:
									Text2.insert(END,"╚")
							if i=="F":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"╪")
								elif RandomNumber==2:
									Text2.insert(END,"Φ")
							if i=="G":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"H")
								elif RandomNumber==2:
									Text2.insert(END,"G")
							if i=="H":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"A")
								elif RandomNumber==2:
									Text2.insert(END,"B")
							if i=="I":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"°")
								elif RandomNumber==2:
									Text2.insert(END,"è")
							if i=="J":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"Ü")
								elif RandomNumber==2:
									Text2.insert(END,"¬")
							if i=="K":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"C")
								elif RandomNumber==2:
									Text2.insert(END,"║")
							if i=="L":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"╩")
								elif RandomNumber==2:
									Text2.insert(END,"┌")
							if i=="M":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"Ω")
								elif RandomNumber==2:
									Text2.insert(END,"·")
							if i=="N":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"N")
								elif RandomNumber==2:
									Text2.insert(END,"Ñ")
							if i=="Ñ":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"ï")
								elif RandomNumber==2:
									Text2.insert(END,"¢")
							if i=="O":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"½")
								elif RandomNumber==2:
									Text2.insert(END,"╗")
							if i=="P":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"╦")
								elif RandomNumber==2:
									Text2.insert(END,"█")
							if i=="Q":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"δ")
								elif RandomNumber==2:
									Text2.insert(END,"√")
							if i=="R":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"î")
								elif RandomNumber==2:
									Text2.insert(END,"£")
							if i=="S":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"¼")
								elif RandomNumber==2:
									Text2.insert(END,"╝")
							if i=="T":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"╠")
								elif RandomNumber==2:
									Text2.insert(END,"▄")
							if i=="U":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"∞")
								elif RandomNumber==2:
									Text2.insert(END,"ⁿ")
							if i=="V":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"ì")
								elif RandomNumber==2:
									Text2.insert(END,"¥")
							if i=="W":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"¡")
								elif RandomNumber==2:
									Text2.insert(END,"╜")
							if i=="X":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"{")
								elif RandomNumber==2:
									Text2.insert(END,")")
							if i=="Y":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"═")
								elif RandomNumber==2:
									Text2.insert(END,"▌")
							if i=="Z":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"φ")
								elif RandomNumber==2:
									Text2.insert(END,"²")
							if i=="Á":
								Text2.insert(END,"Ä")
							if i=="É":
								Text2.insert(END,"«")
							if i=="Í":
								Text2.insert(END,"╛")
							if i=="Ó":
								Text2.insert(END,"╬")
							if i=="Ú":
								Text2.insert(END,"▐")
							if i=="%":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"ε")
								elif RandomNumber==2:
									Text2.insert(END,"■")
							if i=="'":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"Å")
								elif RandomNumber==2:
									Text2.insert(END,"ƒ")
							if i=="$":
								RandomNumber=random.randint(1,2)
								if RandomNumber==1:
									Text2.insert(END,"»")
								elif RandomNumber==2:
									Text2.insert(END,"┐")
							if i=="(":
								Text2.insert(END,"✰")
							if i==")":
								Text2.insert(END,"Ⓐ")
							if i=="@":
								Text2.insert(END,"♬")


						if RandomNumberAlph2==1:
							Text2.insert(END,"…")
						elif RandomNumberAlph2==2:
							Text2.insert(END,"†+")
						elif RandomNumberAlph2==3:
							Text2.insert(END,"₧")
						elif RandomNumberAlph2==4:
							Text2.insert(END,"—")

				elif 75<RandomNumber<=100:
					RandomNumberAlph3=random.randint(1,3)
					Counter2=0
					MidCounter2=0
					MidCounter3=0
					MidCounter4=0
					MidCounter5=0
					if RandomNumberAlph3==1 or RandomNumberAlph3==2 or RandomNumberAlph3==3:
						for i in Text1.get("1.0",END):
							while Counter2!=1:
								if RandomNumberAlph3==1:
									Random=random.randint(1,2)
									if Random==1:
										Text2.insert(END,"⁈")
									elif Random==2:
										Text2.insert(END,"ᶽ")
								elif RandomNumberAlph3==2:
									Random=random.randint(1,2)
									if Random==1:
										Text2.insert(END,"✹")
									elif Random==2:
										Text2.insert(END,"ᵜ")
								elif RandomNumberAlph3==3:
									Random=random.randint(1,2)
									if Random==1:
										Text2.insert(END,"⁇")
									elif Random==2:
										Text2.insert(END,"➻")
								Counter2=+1

							if len(Text2.get("1.0",END))>=8:
								while MidCounter2!=1:
									if RandomNumberAlph3==1:
										Text2.insert(END,"✑")
										MidCounter2=+1
									elif RandomNumberAlph3==2:
										Text2.insert(END,"✫")
										MidCounter2=+1
									elif RandomNumberAlph3==3:
										Text2.insert(END,"☻")
										MidCounter2=+1
							if len(Text2.get("1.0",END))>=100:
								while MidCounter3!=1:
									if RandomNumberAlph3==1:
										Text2.insert(END,"⚥")
										MidCounter3=+1
									elif RandomNumberAlph3==2:
										Text2.insert(END,"❦")
										MidCounter3=+1
									elif RandomNumberAlph3==3:
										Text2.insert(END,"◍")
										MidCounter3=+1
							if len(Text2.get("1.0",END))>=500:
								while MidCounter4!=1:
									if RandomNumberAlph3==1:
										Text2.insert(END,"℮")
										MidCounter4=+1
									elif RandomNumberAlph3==2:
										Text2.insert(END,"✾")
										MidCounter4=+1
									elif RandomNumberAlph3==3:
										Text2.insert(END,"⚘")
										MidCounter4=+1
							if len(Text2.get("1.0",END))>=1000:
								while MidCounter5!=1:
									if RandomNumberAlph3==1:
										Text2.insert(END,"ℓ")
										MidCounter5=+1
									elif RandomNumberAlph3==2:
										Text2.insert(END,"र")
										MidCounter5=+1
									elif RandomNumberAlph3==3:
										Text2.insert(END,"₢")
										MidCounter5=+1
							if i=="a":
								Random=random.randint(1,2)
								if Random==1:
									Text2.insert(END,"ß♙")
								elif Random==2:
									Text2.insert(END,"❅")
							if i=="b":
								Text2.insert(END,"±☤ⓩ")
							if i=="c":
								Text2.insert(END,"a☬")
							if i=="d":
								Text2.insert(END,"b✙")
							if i=="e":
								Text2.insert(END,"➈d⊰")
							if i=="f":
								Text2.insert(END,"⌘c")
							if i=="g":
								Text2.insert(END,"✓E")
							if i=="h":
								Text2.insert(END,"eℬ")
							if i=="i":
								Text2.insert(END,"Fⅺ")
							if i=="j":
								Text2.insert(END,"g☧")
							if i=="k":
								Text2.insert(END,"h﹖")
							if i=="l":
								Text2.insert(END,"⅞é")
							if i=="m":
								Text2.insert(END,"Æ⅟")
							if i=="n":
								Text2.insert(END,"iⓑ")
							if i=="ñ":
								Text2.insert(END,"ó≎≠")
							if i=="o":
								Text2.insert(END,"▓")
							if i=="p":
								Text2.insert(END,"≕≗")
							if i=="q":
								Text2.insert(END,"♡╥")
							if i=="r":
								Text2.insert(END,"j")
							if i=="s":
								Text2.insert(END,"k☾")
							if i=="t":
								Text2.insert(END,"ⓩl")
							if i=="u":
								Text2.insert(END,"m✓")
							if i=="v":
								Text2.insert(END,"n≒")
							if i=="w":
								Text2.insert(END,"┬")
							if i=="x":
								Text2.insert(END,"∱ñ")
							if i=="y":
								Text2.insert(END,"☤o")
							if i=="z":
								Text2.insert(END,"p")
							if i=="!":
								Text2.insert(END,"≒≒q")
							if i=="?":
								Text2.insert(END,"r≝")
							if i=="¿":
								Text2.insert(END,"s☓")
							if i=="¡":
								Text2.insert(END,"t≗")
							if i==".":
								Text2.insert(END,"u∱")
							if i==",":
								Text2.insert(END,"x∬")
							if i==" ":
								Random=random.randint(1,10)
								if Random==1:
									Text2.insert(END,"v⌘")
								if Random==2:
									Text2.insert(END,"Γ")
								if Random==3:
									Text2.insert(END,"∭≥")
								if Random==4:
									Text2.insert(END,"â")
								if Random==5:						
									Text2.insert(END,"ô")
								if Random==6:
									Text2.insert(END,"⇫")
								if Random==7:
									Text2.insert(END,"│")
								if Random==8:
									Text2.insert(END,"├")
								if Random==9:
									Text2.insert(END,"╙")
								if Random==10:
									Text2.insert(END,"π")
							if i=="á":
								Text2.insert(END,"☓≤") 
							if i=="é":
								Text2.insert(END,"☽ä")
							if i=="í":
								Text2.insert(END,"⊰ö")
							if i=="ó":
								Text2.insert(END,"☧┤∭")
							if i=="ú":
								Text2.insert(END,"─ⅵ")
							if i==":":
								Text2.insert(END,"╘")
							if i==";":
								Text2.insert(END,"Σ≛")
							if i=="1":
								Text2.insert(END,"⌠")
							if i=="2":
								Text2.insert(END,"à☽")
							if i=="3":
								Text2.insert(END,"ò")
							if i=="4":
								Text2.insert(END,"H⊱")
							if i=="5":
								Text2.insert(END,"Gⓜ")
							if i=="6":
								Text2.insert(END,"B⋛")
							if i=="7":
								Text2.insert(END,"≩Aⅰ")
							if i=="8":
								Text2.insert(END,"°☃")
							if i=="9":
								Text2.insert(END,"è")
							if i=="0":
								Text2.insert(END,"Ü")
							if i=="A":
								Text2.insert(END,"☓¬")
							if i=="B":
								Text2.insert(END,"C")
							if i=="C":
								Text2.insert(END,"☐║") 
							if i=="D":
								Text2.insert(END,"╩")
							if i=="E":
								Text2.insert(END,"┌")
							if i=="F":
								Text2.insert(END,"Ω")
							if i=="G":
								Text2.insert(END,"·")
							if i=="H":
								Text2.insert(END,"ⅰï")
							if i=="I":
								Text2.insert(END,"¢≣")
							if i=="J":
								Text2.insert(END,"½≖")
							if i=="K":
								Text2.insert(END,"╗")
							if i=="L":
								Text2.insert(END,"╦©")
							if i=="M":
								Text2.insert(END,"█")
							if i=="N":
								Text2.insert(END,"╝")
							if i=="Ñ":
								Text2.insert(END,"╠")
							if i=="O":
								Text2.insert(END,"▄")
							if i=="P":
								Text2.insert(END,"∞≐")
							if i=="Q":
								Text2.insert(END,"ⁿ☐")
							if i=="R":
								Text2.insert(END,"≣ì")
							if i=="S":
								Text2.insert(END,"Ⅲ¥")
							if i=="T":
								Text2.insert(END,"➷¡")
							if i=="U":
								Text2.insert(END,"╜")
							if i=="V":
								Text2.insert(END,"≐═")
							if i=="W":
								Text2.insert(END,"{")
							if i=="X":
								Text2.insert(END,"▌")
							if i=="Y":
								Text2.insert(END,"φ⅞")
							if i=="Z":
								Text2.insert(END,"²Ⅲ")
							if i=="Á":
								Text2.insert(END,"ÄⅯ")
							if i=="É":
								Text2.insert(END,"Ⅲ«")
							if i=="Í":
								Text2.insert(END,"╛ⓜ")
							if i=="Ó":
								Text2.insert(END,"╬")
							if i=="Ú":
								Text2.insert(END,"▐")
							if i=="%":
								Text2.insert(END,"➎ε")
							if i=="'":
								Text2.insert(END,"■")
							if i=="$":
								Text2.insert(END,"Å⅟")
							if i=="(":
								Text2.insert(END,"Y➷")
							if i==")":
								Text2.insert(END,"wⅽ")
							if i=="@":
								Text2.insert(END,"í➁")
			
						if RandomNumberAlph3==1:
							Random=random.randint(1,2)
							if Random==1:
								Text2.insert(END,"☭")
							elif Random==2:
								Text2.insert(END,"▦")
						elif RandomNumberAlph3==2:
							Random=random.randint(1,2)
							if Random==1:
								Text2.insert(END,"✞")
							elif Random==2:
								Text2.insert(END,"⊗")
						elif RandomNumberAlph3==3:
							Random=random.randint(1,2)
							if Random==1:
								Text2.insert(END,"✢")
							elif Random==2:
								Text2.insert(END,"ᶶ")				

		EncryptButton=Button(Frame2,text="Encrypt",command=EncryptFunction,width=9)
		EncryptButton.place(x=260,y=220)

		def DecryptFunction():
			if len(Text1.get("1.0",END))<3:
				messagebox.showwarning("Warning","You cannot decrypt messages with less than 2 characters.")
			else:
				Text2.delete(1.0,END)
				Text2.config(fg="black")
				KeyVarAlph=0
				LengthText=len(Text1.get("1.0",END))


				for i in Text1.get("1.0",END):
					#Alph1 
					if i=="☼":
						for i in Text1.get("1.0",END):
							if i=="‡":
								if LengthText>=280:
									for i in Text1.get("1.0",END):
										if i=="☩":
											KeyVarAlph=1
								else:
									KeyVarAlph=1
					elif i=="♂":
						for i in Text1.get("1.0",END):
							if i=="☓":
								if LengthText>=280:
									for i in Text1.get("1.0",END):
										if i=="♆":
											KeyVarAlph=1
								else:
									KeyVarAlph=1
					elif i=="♫":
						for i in Text1.get("1.0",END):
							if i=="⋆":
								if LengthText>=280:
									for i in Text1.get("1.0",END):
										if i=="ℯ":
											KeyVarAlph=1
								else:
									KeyVarAlph=1
					#Alph2
					if i=="…": 
						for i in Text1.get("1.0",END):
							if i=="♯":
								if LengthText>=280:
									for i in Text1.get("1.0",END):
										if i=="❆":
											KeyVarAlph=2
								else:
									KeyVarAlph=2
					elif i=="₧": 
						for i in Text1.get("1.0",END):
							if i=="﹖":
								if LengthText>=280:
									for i in Text1.get("1.0",END):
										if i=="✆":
											KeyVarAlph=2
								else:
									KeyVarAlph=2
					elif i=="†":
						for i in Text1.get("1.0",END):
							if i=="ϡ":
								if LengthText>=280:
									for i in Text1.get("1.0",END):
										if i=="❅":
											KeyVarAlph=2
								else:
									KeyVarAlph=2
					elif i=="—":
						for i in Text1.get("1.0",END):
							if i=="‽":
								if LengthText>=280:
									for i in Text1.get("1.0",END):
										if i=="☥":
											KeyVarAlph=2
								else:
									KeyVarAlph=2

					#Alph3
					if i=="⁈" or i=="ᶽ":
						for i in Text1.get("1.0",END):
							if i=="☭" or i=="▦":
								if LengthText>=20:
									for i in Text1.get("1.0",END):
										if i=="✑":
											if LengthText>=100:
												for i in Text1.get("1.0",END):
													if i=="⚥":
														if LengthText>=500:
															for i in Text1.get("1.0",END):
																if i=="℮":
																	if LengthText>=1000:
																		for i in Text1.get("1.0",END):
																			if i=="ℓ":
																				KeyVarAlph=3
																	else:
																		KeyVarAlph=3
														else:
															KeyVarAlph=3
											else:
												KeyVarAlph=3	
								else:
									KeyVarAlph=3
					elif i=="✹" or i=="ᵜ":
						for i in Text1.get("1.0",END):
							if i=="✞" or i=="⊗":
								if LengthText>=20:
									for i in Text1.get("1.0",END):
										if i=="✫":
											if LengthText>=100:
												for i in Text1.get("1.0",END):
													if i=="❦":
														if LengthText>=500:
															for i in Text1.get("1.0",END):
																if i=="✾":
																	if LengthText>=1000:
																		for i in Text1.get("1.0",END):
																			if i=="र":
																				KeyVarAlph=3
																	else:
																		KeyVarAlph=3
														else:
															KeyVarAlph=3
											else:
												KeyVarAlph=3
								else:
									KeyVarAlph=3
					elif i=="⁇" or i=="➻":
						for i in Text1.get("1.0",END):
							if i=="✢" or i=="ᶶ":
								if LengthText>=20:
									for i in Text1.get("1.0",END):
										if i=="☻":
											if LengthText>=100:
												for i in Text1.get("1.0",END):
													if i=="◍":
														if LengthText>=500:
															for i in Text1.get("1.0",END):
																if i=="⚘":
																	if LengthText>=1000:
																		for i in Text1.get("1.0",END):
																			if i=="₢":
																				KeyVarAlph=3
																	else:
																		KeyVarAlph=3
														else:
															KeyVarAlph=3
											else:
												KeyVarAlph=3
								else:
									KeyVarAlph=3

				if KeyVarAlph==1:
					for i in Text1.get("1.0",END):
						if i=="!":
							Text2.insert(END,"a")
						if i=="×":
							Text2.insert(END,"a")
						if i=="õ":
							Text2.insert(END,"a")
						if i=="n":
							Text2.insert(END,"b")
						if i=="t":
							Text2.insert(END,"c")
						if i=="q":
							Text2.insert(END,"d")
						if i=="e":
							Text2.insert(END,"e")
						if i=="ç":
							Text2.insert(END,"e")
						if i=="#":
							Text2.insert(END,"f")
						if i=="a":
							Text2.insert(END,"g")
						if i=="v":
							Text2.insert(END,"h")
						if i=="j":
							Text2.insert(END,"i")
						if i=="å":
							Text2.insert(END,"i")
						if i=="ñ":
							Text2.insert(END,"j")
						if i=="<":
							Text2.insert(END,"k")
						if i=="r":
							Text2.insert(END,"l")
						if i=="o":
							Text2.insert(END,"m")
						if i=="¡":
							Text2.insert(END,"n")
						if i=="*":
							Text2.insert(END,"ñ")
						if i=="4":
							Text2.insert(END,"o")
						if i=="ø":
							Text2.insert(END,"o")
						if i=="©":
							Text2.insert(END,"o")
						if i=="s":
							Text2.insert(END,"p")
						if i=="w":
							Text2.insert(END,"q")
						if i=="6":
							Text2.insert(END,"r")
						if i=="î":
							Text2.insert(END,"r")
						if i=="_":
							Text2.insert(END,"s")
						if i=="Ý":
							Text2.insert(END,"s")
						if i=="¶":
							Text2.insert(END,"s")
						if i=="d":
							Text2.insert(END,"t")
						if i=="y":
							Text2.insert(END,"u")
						if i=="Ä":
							Text2.insert(END,"u")
						if i=="x":
							Text2.insert(END,"v")
						if i==")":
							Text2.insert(END,"w")
						if i=="p":
							Text2.insert(END,"x")
						if i=="1":
							Text2.insert(END,"y")
						if i=="f":
							Text2.insert(END,"z")
						if i=="7":
							Text2.insert(END," ")
						if i=="½":
							Text2.insert(END," ")
						if i=="∩":
							Text2.insert(END," ")
						if i=="≥":
							Text2.insert(END," ")
						if i=="≤":
							Text2.insert(END," ")
						if i=="░":
							Text2.insert(END," ")
						if i=="▒":
							Text2.insert(END," ")
						if i=="ε":
							Text2.insert(END," ")
						if i=="≡":
							Text2.insert(END," ")
						if i=="⌡":
							Text2.insert(END," ")
						if i=="¿":
							Text2.insert(END,"!")
						if i=="°":
							Text2.insert(END,"?")
						if i=="%":
							Text2.insert(END,"¿")
						if i=="(":
							Text2.insert(END,"¡")
						if i=="b":
							Text2.insert(END,".")
						if i=="=":
							Text2.insert(END,",")
						if i=="0":
							Text2.insert(END,"á")
						if i=="9":
							Text2.insert(END,"é")
						if i=="2":
							Text2.insert(END,"í")
						if i=="3":
							Text2.insert(END,"ó")
						if i=="&":
							Text2.insert(END,"ú")
						if i=="$":
							Text2.insert(END,":")
						if i=="c":
							Text2.insert(END,"1")
						if i=="l":
							Text2.insert(END,"2")
						if i=="u":
							Text2.insert(END,"3")
						if i=="g":
							Text2.insert(END,"4")
						if i=="→":
							Text2.insert(END,"4")
						if i=="h":
							Text2.insert(END,"5")
						if i=="k":
							Text2.insert(END,"6")
						if i=="z":
							Text2.insert(END,"7")
						if i==">":
							Text2.insert(END,"8")
						if i==";":
							Text2.insert(END,"9")
						if i=="-":
							Text2.insert(END,"0")
						if i=="´":
							Text2.insert(END,"A")
						if i=="⌠":
							Text2.insert(END,"A")
						if i=="Y":
							Text2.insert(END,"B")
						if i=="{":
							Text2.insert(END,"C")
						if i=="¬":
							Text2.insert(END,"D")
						if i=="+":
							Text2.insert(END,"E")
						if i=="U":
							Text2.insert(END,"F")
						if i=="T":
							Text2.insert(END,"G")
						if i=="^":
							Text2.insert(END,"H")
						if i=="R":
							Text2.insert(END,"I")
						if i=="Q":
							Text2.insert(END,"J")
						if i=="P":
							Text2.insert(END,"K")
						if i=="O":
							Text2.insert(END,"L")
						if i=="Ñ":
							Text2.insert(END,"M")
						if i=="N":
							Text2.insert(END,"N")
						if i=="M":
							Text2.insert(END,"Ñ")
						if i=="}":
							Text2.insert(END,"O")
						if i=="K":
							Text2.insert(END,"P")
						if i=="J":
							Text2.insert(END,"Q")
						if i=="I":
							Text2.insert(END,"R")
						if i=="H":
							Text2.insert(END,"S")
						if i=="¨":
							Text2.insert(END,"T")
						if i=="F":
							Text2.insert(END,"U")
						if i=="E":
							Text2.insert(END,"V")
						if i=="D":
							Text2.insert(END,"W")
						if i=="C":
							Text2.insert(END,"X")
						if i=="B":
							Text2.insert(END,"Y")
						if i=="A":
							Text2.insert(END,"Z")
						if i=="É":
							Text2.insert(END,"Á")
						if i=="Á":
							Text2.insert(END,"É")
						if i=="Í":
							Text2.insert(END,"Í")
						if i=="Ú":
							Text2.insert(END,"Ó")
						if i=="Ó":
							Text2.insert(END,"Ú")
						if i=="|":
							Text2.insert(END,"%")
						if i=="♦":
							Text2.insert(END,"(")
						if i=="@":
							Text2.insert(END,"@")
						if i=="↕":
							Text2.insert(END,")")
						if i=="▌":
							Text2.insert(END,"'")
						if i=="▄":
							Text2.insert(END,"$")
						if i=="Θ":
							Text2.insert(END,";")
				elif KeyVarAlph==2:
					for i in Text1.get("1.0",END):
						if i=="○":
							Text2.insert(END,"a")
						if i=="◄":
							Text2.insert(END,"a")
						if i=="‼":
							Text2.insert(END,"a")
						if i=="Ç":
							Text2.insert(END,"b")
						if i=="É":
							Text2.insert(END,"b")
						if i=="á":
							Text2.insert(END,"c")
						if i=="░":
							Text2.insert(END,"c")
						if i=="└":
							Text2.insert(END,"d")
						if i=="╨":
							Text2.insert(END,"d")
						if i=="α":
							Text2.insert(END,"e")
						if i=="≡":
							Text2.insert(END,"e")
						if i=="ü":
							Text2.insert(END,"f")
						if i=="æ":
							Text2.insert(END,"f")
						if i=="í":
							Text2.insert(END,"g")
						if i=="▒":
							Text2.insert(END,"g")
						if i=="┴":
							Text2.insert(END,"h")
						if i=="╤":
							Text2.insert(END,"h")
						if i=="ß":
							Text2.insert(END,"i")
						if i=="±":
							Text2.insert(END,"i")
						if i=="a":
							Text2.insert(END,"j")
						if i=="b":
							Text2.insert(END,"j")
						if i=="d":
							Text2.insert(END,"k")
						if i=="c":
							Text2.insert(END,"k")
						if i=="→":
							Text2.insert(END,"l")
						if i=="e":
							Text2.insert(END,"l")
						if i=="F":
							Text2.insert(END,"m")
						if i=="g":
							Text2.insert(END,"m")
						if i=="h":
							Text2.insert(END,"m")
						if i=="é":
							Text2.insert(END,"n")
						if i=="Æ":
							Text2.insert(END,"n")
						if i=="i":
							Text2.insert(END,"ñ")
						if i=="ó":
							Text2.insert(END,"o")
						if i=="▓":
							Text2.insert(END,"o")
						if i=="┬":
							Text2.insert(END,"p")
						if i=="╥":
							Text2.insert(END,"p")
						if i=="j":
							Text2.insert(END,"q")
						if i=="k":
							Text2.insert(END,"q")
						if i=="l":
							Text2.insert(END,"r")
						if i=="m":
							Text2.insert(END,"r")
						if i=="n":
							Text2.insert(END,"s")
						if i=="ñ":
							Text2.insert(END,"s")
						if i=="o":
							Text2.insert(END,"t")
						if i=="p":
							Text2.insert(END,"t")
						if i=="q":
							Text2.insert(END,"u")
						if i=="r":
							Text2.insert(END,"u")
						if i=="s":
							Text2.insert(END,"v")
						if i=="t":
							Text2.insert(END,"v")
						if i=="u":
							Text2.insert(END,"w")
						if i=="x":
							Text2.insert(END,"w")
						if i=="v":
							Text2.insert(END,"x")
						if i=="Γ":
							Text2.insert(END,"x")
						if i=="≥":
							Text2.insert(END,"x")
						if i=="â":
							Text2.insert(END,"y")
						if i=="ô":
							Text2.insert(END,"y")
						if i=="ú":
							Text2.insert(END,"z")
						if i=="│":
							Text2.insert(END,"z")
						if i=="├":
							Text2.insert(END,"!")
						if i=="╙":
							Text2.insert(END,"!")
						if i=="π":
							Text2.insert(END,"?")
						if i=="≤":
							Text2.insert(END,"?")
						if i=="ä":
							Text2.insert(END,"¿")
						if i=="ö":
							Text2.insert(END,"¿")
						if i=="┤":
							Text2.insert(END,"¡")
						if i=="─":
							Text2.insert(END,"¡")
						if i=="╘":
							Text2.insert(END,".")
						if i=="Σ":
							Text2.insert(END,".")
						if i=="⌠":
							Text2.insert(END,".")
						if i=="à":
							Text2.insert(END,",")
						if i=="ò":
							Text2.insert(END,",")
						if i=="╡":
							Text2.insert(END," ")
						if i=="┼":
							Text2.insert(END," ")
						if i=="╒":
							Text2.insert(END," ")
						if i=="σ":
							Text2.insert(END," ")
						if i=="⌡":
							Text2.insert(END," ")
						if i=="å":
							Text2.insert(END,"á")
						if i=="û":
							Text2.insert(END,"é")
						if i=="ª":
							Text2.insert(END,"í")
						if i=="╢":
							Text2.insert(END,"ó")
						if i=="╞":
							Text2.insert(END,"ú")
						if i=="╓":
							Text2.insert(END,":")
						if i=="µ":
							Text2.insert(END,";")
						if i=="÷":
							Text2.insert(END,"1")
						if i=="8":
							Text2.insert(END,"1")
						if i=="ç":
							Text2.insert(END,"2")
						if i=="≈":
							Text2.insert(END,"2")
						if i=="ù":
							Text2.insert(END,"3")
						if i=="9":
							Text2.insert(END,"4")
						if i=="º":
							Text2.insert(END,"5")
						if i=="τ":
							Text2.insert(END,"5")
						if i=="╖":
							Text2.insert(END,"6")
						if i=="3":
							Text2.insert(END,"7")
						if i=="2":
							Text2.insert(END,"8")
						if i=="╟":
							Text2.insert(END,"9")
						if i=="╫":
							Text2.insert(END,"0")
						if i=="1":
							Text2.insert(END,"0")
						if i=="ê":
							Text2.insert(END,"A")
						if i=="E":
							Text2.insert(END,"A")
						if i=="f":
							Text2.insert(END,"B")
						if i=="Á":
							Text2.insert(END,"B")
						if i=="ÿ":
							Text2.insert(END,"C")
						if i=="¿":
							Text2.insert(END,"C")
						if i=="z":
							Text2.insert(END,"D")
						if i=="Z":
							Text2.insert(END,"D")
						if i=="╕":
							Text2.insert(END,"E")
						if i=="╚":
							Text2.insert(END,"E")
						if i=="╪":
							Text2.insert(END,"F")
						if i=="Φ":
							Text2.insert(END,"F")
						if i=="H":
							Text2.insert(END,"G")
						if i=="G":
							Text2.insert(END,"G")
						if i=="A":
							Text2.insert(END,"H")
						if i=="B":
							Text2.insert(END,"H")
						if i=="°":
							Text2.insert(END,"I")
						if i=="è":
							Text2.insert(END,"I")
						if i=="Ü":
							Text2.insert(END,"J")
						if i=="¬":
							Text2.insert(END,"J")
						if i=="C":
							Text2.insert(END,"K")
						if i=="║":
							Text2.insert(END,"K")
						if i=="╩":
							Text2.insert(END,"L")
						if i=="┌":
							Text2.insert(END,"L")
						if i=="Ω":
							Text2.insert(END,"M")
						if i=="·":
							Text2.insert(END,"M")
						if i=="N":
							Text2.insert(END,"N")
						if i=="Ñ":
							Text2.insert(END,"N")
						if i=="ï":
							Text2.insert(END,"Ñ")
						if i=="¢":
							Text2.insert(END,"Ñ")
						if i=="½":
							Text2.insert(END,"O")
						if i=="╗":
							Text2.insert(END,"O")
						if i=="╦":
							Text2.insert(END,"P")
						if i=="█":
							Text2.insert(END,"P")
						if i=="δ":
							Text2.insert(END,"Q")
						if i=="√":
							Text2.insert(END,"Q")
						if i=="î":
							Text2.insert(END,"R")
						if i=="£":
							Text2.insert(END,"R")
						if i=="¼":
							Text2.insert(END,"S")
						if i=="╝":
							Text2.insert(END,"S")
						if i=="╠":
							Text2.insert(END,"T")
						if i=="▄":
							Text2.insert(END,"T")
						if i=="∞":
							Text2.insert(END,"U")
						if i=="ⁿ":
							Text2.insert(END,"U")
						if i=="ì":
							Text2.insert(END,"V")
						if i=="¥":
							Text2.insert(END,"V")
						if i=="¡":
							Text2.insert(END,"W")
						if i=="╜":
							Text2.insert(END,"W")
						if i=="{":
							Text2.insert(END,"X")
						if i==")":
							Text2.insert(END,"X")
						if i=="═":
							Text2.insert(END,"Y")
						if i=="▌":
							Text2.insert(END,"Y")
						if i=="φ":
							Text2.insert(END,"Z")
						if i=="²":
							Text2.insert(END,"Z")
						if i=="Ä":
							Text2.insert(END,"Á")
						if i=="«":
							Text2.insert(END,"É")
						if i=="╛":
							Text2.insert(END,"Í")
						if i=="╬":
							Text2.insert(END,"Ó")
						if i=="▐":
							Text2.insert(END,"Ú")
						if i=="ε":
							Text2.insert(END,"%")
						if i=="■":
							Text2.insert(END,"%")
						if i=="Å":
							Text2.insert(END,"'")
						if i=="ƒ":
							Text2.insert(END,"'")
						if i=="»":
							Text2.insert(END,"$")
						if i=="┐":
							Text2.insert(END,"$") 
						if i=="✰":
							Text2.insert(END,"(") 
						if i=="Ⓐ":
							Text2.insert(END,")") 
						if i=="♬":
							Text2.insert(END,"@") 
				elif KeyVarAlph==3:
					for i in Text1.get("1.0",END):
						if i=="ß":
							Text2.insert(END,"a") 
						if i=="❅":
							Text2.insert(END,"a")
						if i=="±":
							Text2.insert(END,"b")
						if i=="a":
							Text2.insert(END,"c")
						if i=="b":
							Text2.insert(END,"d")
						if i=="d":
							Text2.insert(END,"e")
						if i=="c":
							Text2.insert(END,"f")
						if i=="E":
							Text2.insert(END,"g")
						if i=="e":
							Text2.insert(END,"h")
						if i=="F":
							Text2.insert(END,"i")
						if i=="g":
							Text2.insert(END,"j")
						if i=="h":
							Text2.insert(END,"k")
						if i=="é":
							Text2.insert(END,"l")
						if i=="Æ":
							Text2.insert(END,"m")
						if i=="i":
							Text2.insert(END,"n")
						if i=="ó":
							Text2.insert(END,"ñ")
						if i=="▓":
							Text2.insert(END,"o")
						if i=="≕":
							Text2.insert(END,"p")
						if i=="╥":
							Text2.insert(END,"q")
						if i=="j":
							Text2.insert(END,"r")
						if i=="k":
							Text2.insert(END,"s")
						if i=="l":
							Text2.insert(END,"t")
						if i=="m":
							Text2.insert(END,"u")
						if i=="n":
							Text2.insert(END,"v")
						if i=="┬":
							Text2.insert(END,"w")
						if i=="ñ":
							Text2.insert(END,"x")
						if i=="o":
							Text2.insert(END,"y")
						if i=="p":
							Text2.insert(END,"z")
						if i=="q":
							Text2.insert(END,"!")
						if i=="r":
							Text2.insert(END,"?")
						if i=="s":
							Text2.insert(END,"¿")
						if i=="t":
							Text2.insert(END,"¡")
						if i=="u":
							Text2.insert(END,".")
						if i=="x":
							Text2.insert(END,",")
						if i=="v":
							Text2.insert(END," ")
						if i=="Γ":
							Text2.insert(END," ")
						if i=="≥":
							Text2.insert(END," ")
						if i=="â":
							Text2.insert(END," ")
						if i=="ô":
							Text2.insert(END," ")
						if i=="⇫":
							Text2.insert(END," ")
						if i=="│":
							Text2.insert(END," ")
						if i=="├":
							Text2.insert(END," ")
						if i=="╙":
							Text2.insert(END," ")
						if i=="π":
							Text2.insert(END," ")
						if i=="≤":
							Text2.insert(END,"á")
						if i=="ä":
							Text2.insert(END,"é")
						if i=="ö":
							Text2.insert(END,"í")
						if i=="┤":
							Text2.insert(END,"ó")
						if i=="─":
							Text2.insert(END,"ú")
						if i=="╘":
							Text2.insert(END,":")
						if i=="Σ":
							Text2.insert(END,";")
						if i=="⌠":
							Text2.insert(END,"1")
						if i=="à":
							Text2.insert(END,"2")
						if i=="ò":
							Text2.insert(END,"3")
						if i=="H":
							Text2.insert(END,"4")
						if i=="G":
							Text2.insert(END,"5")
						if i=="B":
							Text2.insert(END,"6")
						if i=="A":
							Text2.insert(END,"7")
						if i=="°":
							Text2.insert(END,"8")
						if i=="è":
							Text2.insert(END,"9")
						if i=="Ü":
							Text2.insert(END,"0")
						if i=="¬":
							Text2.insert(END,"A")
						if i=="C":
							Text2.insert(END,"B")
						if i=="║":
							Text2.insert(END,"C")
						if i=="╩":
							Text2.insert(END,"D")
						if i=="┌":
							Text2.insert(END,"E")
						if i=="Ω":
							Text2.insert(END,"F")
						if i=="·":
							Text2.insert(END,"G")
						if i=="ï":
							Text2.insert(END,"H")
						if i=="¢":
							Text2.insert(END,"I")
						if i=="½":
							Text2.insert(END,"J")
						if i=="╗":
							Text2.insert(END,"K")
						if i=="╦":
							Text2.insert(END,"L")
						if i=="█":
							Text2.insert(END,"M")
						if i=="╝":
							Text2.insert(END,"N")
						if i=="╠":
							Text2.insert(END,"Ñ")
						if i=="▄":
							Text2.insert(END,"O")
						if i=="∞":
							Text2.insert(END,"P")
						if i=="ⁿ":
							Text2.insert(END,"Q")
						if i=="ì":
							Text2.insert(END,"R")
						if i=="¥":
							Text2.insert(END,"S")
						if i=="¡":
							Text2.insert(END,"T")
						if i=="╜":
							Text2.insert(END,"U")
						if i=="═":
							Text2.insert(END,"V")
						if i=="{":
							Text2.insert(END,"W")
						if i=="▌":
							Text2.insert(END,"X")
						if i=="φ":
							Text2.insert(END,"Y")
						if i=="²":
							Text2.insert(END,"Z")
						if i=="Ä":
							Text2.insert(END,"Á")
						if i=="«":
							Text2.insert(END,"É")
						if i=="╛":
							Text2.insert(END,"Í")
						if i=="╬":
							Text2.insert(END,"Ó")
						if i=="▐":
							Text2.insert(END,"Ú")
						if i=="ε":
							Text2.insert(END,"%")
						if i=="■":
							Text2.insert(END,"'")
						if i=="Å":
							Text2.insert(END,"$")
						if i=="Y":
							Text2.insert(END,"(")
						if i=="w":
							Text2.insert(END,")")
						if i=="í":
							Text2.insert(END,"@")
					
				elif KeyVarAlph==0:
					Text2.insert(END,"Encryption incomplete.")
					Text2.config(fg="red")
					messagebox.showwarning("Warning","Incorrect encryption.\nVerify if the encyrption is correct.")
		#Buttons Erase and Copy
		def Function_ClearG():
			Text1.delete(1.0,END)
			Text2.delete(1.0,END)
		ButtonClearG=Button(Frame2,text="Clear all",command=Function_ClearG)
		ButtonClearG.place(x=322,y=430)

		def Function_Clear1():
			Text1.delete(1.0,END)
		ButtonClear1=Button(Frame2,text="Clear",command=Function_Clear1)
		ButtonClear1.place(x=100,y=200)

		def Function_Clear2():			
			Text2.delete(1.0,END)
		ButtonClear2=Button(Frame2,text="Clear",command=Function_Clear2)
		ButtonClear2.place(x=100,y=410)

		def Copy1():
			Root.clipboard_clear()
			Root.clipboard_append(str(Text1.get("1.0",END)))
			Root.update()
		ButtonCopy1=Button(Frame2,text="Copy",command=Copy1)
		ButtonCopy1.place(x=555,y=200)

		def Copy2():
			Root.clipboard_clear()
			Root.clipboard_append(str(Text2.get("1.0",END)))
			Root.update()
		ButtonCopy2=Button(Frame2,text="Copy",command=Copy2)
		ButtonCopy2.place(x=555,y=410)

		DecryptButton=Button(Frame2,text="Decrypt",command=DecryptFunction,width=10)
		DecryptButton.place(x=360,y=220)

		Root.mainloop()
		
	else:
		WrongPass=Label(Frame1,text="Wrong password")
		WrongPass.config(fg="red")
		WrongPass.place(x=155,y=140)

SendButton=Button(Frame1,text="Send",command=SendFunction)
SendButton.place(x=178,y=180)
SendButton.config(font=("Arial",11))

#ButtonExit
def Exitfunction():
	Decision=messagebox.askquestion("Exit","Would you like to quit the program?")
	if Decision=="yes":
		Root.destroy()
ExitButton=Button(Frame1,text="Exit",command=Exitfunction)
ExitButton.place(x=5,y=5)

#ButtonInfo
def InfoFunction():
	messagebox.showinfo("Information",'''Enter the password and click on the button that reads "Send" afterwards.''')
InfoButton=Button(Frame1,text="Info",command=InfoFunction)
InfoButton.place(x=360,y=5)

Root.mainloop()