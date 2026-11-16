print("please enter a symptom from fever, cough, headache, cold, stomach_pain")
Symptom = str(input("enter the symptom: "))
suggestion = {"fever": "visit a doctor","cough": "drink warm water","headache": "drink more and more water","cold": "take rest","stomach_pain": "take medicine"}
if Symptom in suggestion:
    print(suggestion[Symptom])
else:
    print("no symptoms matched please concern a doctor")