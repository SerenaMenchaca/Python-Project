#project

#project opener
print 'It was long ago, precisely 45 A.D. King Certifacato sends a knight to go get you. This is where you come in. By the way what is your name?'
userInput = raw_input()
print 'Knight: Have you seen a youg man named ' + str(userInput)
print str(userInput) + ': That is me'
print 'Knight: Oh... Then come with me King Certifacato needs you.'
#Going to see the king

print '(You go with the knight to see the king)'

print '(The king sees you walk in and sends his servants that are surrounding him away.)'
print 'King Certifacato: You must be ' + str(userInput)
print str(userInput) + ': Yes that`s me your majesty. Why did you need me?'
print 'King Certifacato: Did you know your granfather ' + str(userInput)   
 
userAnswer1 = raw_input()
if userAnswer1 == str('yes'):
    print 'King Certifacato: Then you knew that your grandfather was a great knight.'
elif userAnswer1 == str('no'):
    print 'King Certifacato: Ok well your grandfather was the greastest knight that has ever fought for this kingdom.' 



