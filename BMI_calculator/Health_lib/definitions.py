# -*- coding: utf-8 -*-
from utilz import printer

#below functions are called by bmi()
def severe_underweight():			
	printer("You are severely underweight\nYou should consult your physician to determine if you should gain weight.")
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* Inhibited growth and development, especially for children and teens.\n* Fragile bones, deficiency in vitamin D and calcium along with low body weight can lead to osteoporosis.\n* Weakened immune system, your body cannot store energy and may also have difficulty fighting and bouncing back from illness.\n* Anemia caused by iron, folate and vitamin B12 deficiency, resulting in dizziness, fatigue and headaches.\n* Fertility issues. In women, low body weight can lead to irregular or lack of periods and infertility.\n* Hair loss, dry thin skin and teeth health issues.")
		result2=raw_input("\nDo you want to find out what the causes are? > ")
	if result2 !="n":
		printer("* Genetics - runs in your family, it's likely that you were born with a higher-than-usual metabolism.\n* High physical activity burns more calories.\n* Illness can affect your appetite, as well as your body's ability to use and store food. \n* Certain prescription medicines and treatments can cause nausea and weight loss.\n* Psychological Issues like stress, depression, anorexia, etc can disrupt healthy eating habits.")
		result3=raw_input("\nDo you want to find out about treatment? > ")
	if result3!="n":
		printer("* Add healthy calories without radically changing your diet eg: nut or seed toppings, cheese, healthy side dishes, fruit or whole-grain wheat toast.\n* Go nutrient dense. High-protein meats, which can help you to build muscle and nutritious carbohydrates, such as brown rice and other whole grains. \n* Snack away on protein and healthy carbohydrates.eg: trail mix, protein bars or drinks, and crackers with hummus or peanut butter. \n* If you have poor appetite, eat mini-meals throughout the day to increase your calorie intake.\n* Bulk up - strength training, such as weight-lifting or yoga, can help you gain weight by building muscle. ")

def underweight():
	printer("You are underweight.")
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* If you happen to lose more weight due to illness, stress or habits like smoking and poor diet, you may get:\n* Anemia, viz caused by iron, folate and vitamin B12 deficiency, resulting in dizziness, fatigue and headaches.\n* Fertility issues. In women, low body weight can lead to irregular or lack of periods and infertility.\n* Hair loss, dry thin skin and teeth health issues.")
	result2=raw_input("\nDo you want to find out what the causes are? > ")
	if result2 !="n":
		printer("* Genetics - runs in your family, it's likely that you were born with a higher-than-usual metabolism.\n* High physical activity burns more calories.")
	result3=raw_input("\nDo you want to find out how to gain weight? > ")
	if result3!="n":
		printer("* Continue your regular balanced diet or switch over to one if you don't eat regularly.\n* Bulk up - strength training, such as weight-lifting or yoga, can help you gain muscle.")
	
def normal():
		printer("You are normal weight :)")


def overweight():
	printer("You are overweight")	
	result=raw_input("\nDo you want some tips to reduce weight? > ")
	if result!="n":
		printer("* So what if you have some fudge in the pudge. You're just working out and eating clean to become the best version of you(not that you already aren't)\n* First step is to slowly taper the sugar and processed food intake and improve your stamina by taking long walks.\n* Choose healthy meal options, like dark chocolate instead of candy, sugar-free options containing stevia and fruit if you have a sweet-tooth.\n* After you build your stamina, take up fun workout routines like dancing, swimming, beginner's zumba, etc.\n* If aerobics is not your thing, try weight lifting, even if you are a chick. It burns fat and builds muscle. And don't worry, you can always slow down if you find yourself bulking up to much.")
		result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1!="n":
		printer("* If your BMI is above 32.5, you may experience a general fatigue and lack of stamina. Being a little overweight is not unhealthy!")

		
		
def moderately_obese():	
	printer("You are moderately obese")
	result=raw_input("\nDo you want some tips to reduce weight? > ")
	if result!="n":
		printer("* Great! First step is to slowly taper the sugar and processed food intake and improve your stamina by taking long walks.\n* Choose healthy meal options, like dark chocolate instead of candy, sugar-free options containing stevia and fruit if you have a sweet-tooth.\n* Keep a food journal if you are serious about losing weight. Note down everything you ate that day.\n* Have your friends/parents support you in this ourney and ask them to switch to healthier options too!\n* After you build your stamina, take up fun workout routines like dancing, swimming, beginner's zumba, etc.\n*  If aerobics is not your thing, try weight lifting, even if you are a chick. It burns fat and builds muscle. And don't worry, you can always slow down if you find yourself bulking up to much.\n* Stay positive. So what if you have some fudge in the pudge. You can lose it in no time! Stay motivated.\n* Drink a lot of water.\n* If you don't think you can survive without meat, switch to ketogenic diet. If you think you can't survive without carbs, switch to a balanced low calorie diet.")
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* You would experience a general fatigue and lack of stamina.\n* It makes you more likely to have conditions including heart disease and stroke, high blood pressure, Diabetes, some cancers, Gallbladder disease and gallstones, Osteoarthritis, Gout, breathing problems, such as sleep apnea (when a person stops breathing for short episodes during sleep) and asthma.\n* You should consult your physician to determine if you are suffering any of these conditions.")
	result2=raw_input("\nDo you want to find out what causes this? > ")
	if result2 !="n":
		printer("* Behavioral factors like your eating habits and daily activity level. Many people develop their eating habits as children and have trouble refining them to maintain proper body weight as they age. As an adult, you may be inactive at your job and have less time for exercise, meal planning, and physical activity.\n* Stress, anxiety, and lack of sleep, can lead to weight gain. People who quit smoking often experience temporary weight gain. Women may also have trouble losing the weight they gain during pregnancy or gain additional weight during menopause.\n* Certain medications eg:birth control pills and antidepressants, can cause weight gain.\n* Genetic factors may control how your body stores energy.")
			
			
def extremely_obese():
	printer("You are extremely obese")
	result=raw_input("\nDo you want some tips to reduce weight? > ")
	if result!="n":
		printer("* Great! First step is to slowly taper the sugar and processed food intake and improve your stamina by taking long walks.\n* Choose healthy meal options, like dark chocolate instead of candy, sugar-free options containing stevia and fruit if you have a sweet-tooth.\n* Keep a food journal if you are serious about losing weight. Note down everything you ate that day.\n* Have your friends/parents support you in this ourney and ask them to switch to healthier options too!\n* After you build your stamina, take up fun workout routines like dancing, swimming, beginner's zumba, etc.\n* Stay positive. Keep yourself motivated and make realistic goals.\n* If you are battling depression, join a support group, get involved in community activities or go for meditation classes.\n* Drink a lot of water or chicken/tomato soup.\n* Find a job that does not involve food, ideally something you like doing. No matter what it is, if you are not just sitting at home and watching TV, you are less likely to eat.")
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* You would experience a general fatigue and lack of stamina.\n* It makes you more likely to have conditions including heart disease and stroke, high blood pressure, Diabetes, some cancers, Gallbladder disease and gallstones, Osteoarthritis, Gout, breathing problems, such as sleep apnea (when a person stops breathing for short episodes during sleep) and asthma.\n* You should consult your physician to determine if you are suffering any of these conditions.")
	result2=raw_input("\nDo you want to find out what causes this? > ")
	if result2 !="n":
		printer("* Behavioral factors like your eating habits and daily activity level. Many people develop their eating habits as children and have trouble refining them to maintain proper body weight as they age. As an adult, you may be inactive at your job and have less time for exercise, meal planning, and physical activity.\n* Stress, anxiety, and lack of sleep, can lead to weight gain. People who quit smoking often experience temporary weight gain. Women may also have trouble losing the weight they gain during pregnancy or gain additional weight during menopause.\n* Certain medications eg:birth control pills and antidepressants, can cause weight gain.\n* Genetic factors may control how your body stores energy.")


def morbidly_obese():
	printer("You are morbidly obese")
	result=raw_input("\nDo you want some tips to reduce weight? > ")
	if result!="n":
		print"When you have a lot of weight to lose, it means playing the long game. You have to chart out a game-plan to cut calories, fight the hunger pangs, make exercise easier, stay on track, and more.\n* Slowly taper the sugar and processed food intake and improve your stamina by taking long walks.\n* If walks hurt your knees, try physical therapy. They'll design a program tailored for you to improve your balance and range of motion.\n* Choose healthy meal options, like dark chocolate instead of candy, sugar-free options containing stevia and fruit if you have a sweet-tooth.People who eat more in the morning and less at night tend to lose more weight. High-protein, warm, solid meal(350-400 calories with at least 25 grams of protein) helps you feel fuller and less hungry later.\n* Keep a photo food ounal on your phone, that you can erase every two weeks. They'll remind you of what you've eaten.\n* If you are battling depression, join a support group, get involved in community activities or go for meditation classes.\n* Drink a lot of water or chicken/tomato soup.\n* Find a job that does not involve food, ideally something you like doing. No matter what it is, if you are not just sitting at home and watching TV, you are less likely to eat.\n* Set Up Your Food Storage. After you purge your home of those treats you can't resist, assign shelves in the pantry and the fridge so your healthy food becomes easy to see and reach.\n* Get checked for sleep apnea. This condition can disrupt your slumber and you won't know it. Studies show that a lack of sleep alters hormones that control hunger.\n* Weight loss surgery should be your last option if you don't see any changes in 5-6 months time."
	result1=raw_input("\nDo you want to find out problems this causes? > ")
	if result1 !="n":
		printer("* You would experience a general fatigue and lack of stamina.\n* It makes you more likely to have conditions including heart disease and stroke, high blood pressure, Diabetes, some cancers, Gallbladder disease and gallstones, Osteoarthritis, Gout, breathing problems, such as sleep apnea (when a person stops breathing for short episodes during sleep) and asthma.\n* You should consult your physician to determine if you are suffering any of these conditions.")
	result2=raw_input("\nDo you want to find out what causes this? > ")
	if result2 !="n":
		printer("* Behavioral factors like your eating habits and daily activity level. Many people develop their eating habits as children and have trouble refining them to maintain proper body weight as they age. As an adult, you may be inactive at your job and have less time for exercise, meal planning, and physical activity.\n* Stress, anxiety, and lack of sleep, can lead to weight gain. People who quit smoking often experience temporary weight gain. Women may also have trouble losing the weight they gain during pregnancy or gain additional weight during menopause.\n* Certain medications eg:birth control pills and antidepressants, can cause weight gain.\n* Genetic factors may control how your body stores energy.")
		
