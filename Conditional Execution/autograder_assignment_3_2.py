'''
This code provides grade using conditional statement on the basis of following criteria:
'''

score = float(input("Enter Score: "))
X = 'Error'

if score >= 0.9: # Example input: 0.95
    X = 'A'
elif score >=0.8: # Example input: 0.85
    X ='B'
elif score >=0.7: # Example input: 0.75
    X ='C'
elif score >= 0.6: # Example input: 0.65
    X ='D'
elif score < .6: # Example input: 0.5
    X ='F'
else: # Example input: 1.1
    X ="Out of Range"

print (X)
