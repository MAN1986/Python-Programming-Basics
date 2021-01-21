# Task of Bowling Figures.
#Overs-Maiden-Runs-Wickets
bowling="""Wasim Akram	: 10-0-49-3 
    Aaqib Javed: 10- 2-77-2
    Mushtaq Ahmed:10- 1-41-3
    Ijaz Ahmed:3-0-13-0
    Imran Khan:6.2-0-43- 1
    Aamer Sohail	: 10-0-49 -0"""
# # Display Name of the Bowler with best economy (min runs per over).
# # Display Total Maiden Overs by Pakistan Team
# # Total Overs bowled by Pakistan Team
bowlingList=bowling.splitlines()
a=[rec.replace(':','-') for rec in bowlingList]
b=[rec.split('-') for rec in a]
c=[[item.strip() for item in rec] for rec in b]
# c=[]
# for rec in b:
#     sub=[]
#     for item in rec:
#         sub.append(item.strip())
#     c.append(sub)

#['Wasim Akram', '10', '0', '49', '3']
economy=[(int(r)/float(o),n) for n,o,m,r,w in c]
print(min(economy)[1])