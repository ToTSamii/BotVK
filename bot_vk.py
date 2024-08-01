import vk_api, time, json, random
from vk_api.longpoll import VkLongPoll, VkEventType
token = ""

vk_session = vk_api.VkApi(token = token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def button(text, color):
	return{
		"action":{
			"type": "text",
			"payload": "{\"button\": \"" + "1" + "\"}",
			"label": f"{text}"
		},
		"color": f"{color}"			
	}
keyboard1 = {
 	"one_time": False,
 	"buttons":[
 		[button("Онлайн школа - DePromotion","positive")],
 		[button("Онлайн каталог товаров - DeMarket","positive")],
 		[button("Сервис поиска работы - DeWork","positive")],
 		[button("Сервис услуг - DeService","positive")],
 		[button("B2B услуги - DeBusiness","primary")]
 		]
 	 }
keyboard2 = {
 	"one_time": False,
 	"buttons":[
		[button("IT сфера","positive")],[button("Маркетинг","positive")],[button("Таргетинг","positive")],[button("Продажи","positive")],
 		[button("Менеджмент","positive")],[button("Коммерческая стратегия","positive")],[button("Инвестиции","positive")],[button("Политология","positive")],
 		[button("Вернуться к началу","negative")]
 		]
 	 }
keyboard3 = {
 	"one_time": False,
 	"buttons":[
 		[button("","")],
 		]
 	 }
keyboard4 = {
 	"one_time": False,
 	"buttons":[
 		[button("","")],
 		]
 	 }
keyboard5 = {
 	"one_time": False,
 	"buttons":[
 		[button("","")],
 		]
 	 } 	 
keyboard6 = {
 	"one_time": False,
 	"buttons":[
 		[button("","")],
 		]
 	 }
keyboard7 = {
 	"one_time": False,
 	"buttons":[
 		[button("","")],
 		]
 	 }
keyboard8 = {
 	"one_time": False,
 	"buttons":[
 		[button("Тарифы","positive")],
 		[button("Назад","negative")]
 		]
 	 }
keyboard9 = {
 	"one_time": False,
 	"buttons":[
 		[button("Low","positive")],[button("LowMax","positive")],[button("Medium","positive")],[button("MediumMax","positive")],
 		[button("LowProMax","positive")],[button("MediumProMax","positive")],[button("High","positive")],[button("HighMax","positive")],
 		[button("Назад","negative")]
 		]
 	 }

keyboard1 = json.dumps(keyboard1, ensure_ascii = False).encode("utf-8")
keyboard1 = str(keyboard1.decode("utf-8"))
keyboard2 = json.dumps(keyboard2, ensure_ascii = False).encode("utf-8")
keyboard2 = str(keyboard2.decode("utf-8"))
keyboard3 = json.dumps(keyboard3, ensure_ascii = False).encode("utf-8")
keyboard3 = str(keyboard3.decode("utf-8"))
keyboard4 = json.dumps(keyboard4, ensure_ascii = False).encode("utf-8")
keyboard4 = str(keyboard4.decode("utf-8"))
keyboard5 = json.dumps(keyboard5, ensure_ascii = False).encode("utf-8")
keyboard5 = str(keyboard5.decode("utf-8"))
keyboard6 = json.dumps(keyboard6, ensure_ascii = False).encode("utf-8")
keyboard6 = str(keyboard6.decode("utf-8"))
keyboard7 = json.dumps(keyboard7, ensure_ascii = False).encode("utf-8")
keyboard7 = str(keyboard7.decode("utf-8"))
keyboard8 = json.dumps(keyboard8, ensure_ascii = False).encode("utf-8")
keyboard8 = str(keyboard8.decode("utf-8"))
keyboard9 = json.dumps(keyboard9, ensure_ascii = False).encode("utf-8")
keyboard9 = str(keyboard9.decode("utf-8"))

def sender1(id, text):
	vk_session.method("messages.send",{"user_id":id, "message": text, "random_id":0, "keyboard": keyboard1})
def sender2(id, text):
	vk_session.method("messages.send",{"user_id":id, "message": text, "random_id":0, "keyboard": keyboard2})
def sender3(id, text):
	vk_session.method("messages.send",{"user_id":id, "message": text, "random_id":0, "keyboard": keyboard3})
def sender4(id, text):
	vk_session.method("messages.send",{"user_id":id, "message": text, "random_id":0, "keyboard": keyboard4})
def sender5(id, text):
	vk_session.method("messages.send",{"user_id":id, "message": text, "random_id":0, "keyboard": keyboard5})
def sender6(id, text):
	vk_session.method("messages.send",{"user_id":id, "message": text, "random_id":0, "keyboard": keyboard6})
def sender7(id, text):
	vk_session.method("messages.send",{"user_id":id, "message": text, "random_id":0})
def sender8(id, text):
	vk_session.method("messages.send",{"user_id":id, "message": text, "random_id":0, "keyboard": keyboard8})
def sender9(id, text):
	vk_session.method("messages.send",{"user_id":id, "message": text, "random_id":0, "keyboard": keyboard9})

for event in longpoll.listen():
	if event.type ==  VkEventType.MESSAGE_NEW:		
		if event.to_me:
			msg = event.text.lower()
			id = event.user_id
			if msg == "начать":
				sender1(id,"Выберите то, что для вас нужно")
			elif msg == "онлайн школа - depromotion":
				sender2(id, "DePromotion - это онлайн школа, в которой вы сможете получить новые знания в той или иной области.\n"
					"Нажмите на ту клавишу, которая вам больше подходит")
			elif msg == "онлайн каталог товаров - demarket":
				sender3(id,"DeMarket - это онлайн каталог товаров продукции из разных сигментов\n"
					"Нажмите на ту клавишу, которая вам больше подходит")
			elif msg == "b2b услуги - debusiness":
				sender4(id,"DeBusiness - это услуги для бизнеса.\n"
					"Нажмите на ту клавишу, которая вам больше подходит")
			elif msg == "сервис поиска работы - dework":
				sender5(id,"DeWork - это сервис поиска работ.\n"
					"Нажмите на ту клавишу, которая вам больше подходит")
			elif msg == "сервис услуг - deservice":
				sender6(id,"DeService - это сервис услуг\n"
					"Нажмите на ту клавишу, которая вам больше подходит")
			elif msg == "вернуться к началу":
				sender1(id,"Выберите то, что для вас нужно")
			elif msg == "назад":
				sender2(id,"Назад")
			
			elif msg == "it сфера":
				sender8(id,"IT-сфера - это отрасль, которая отвечает за обработку, сбор, хранение и передачу информации с помощью технических устройств и вычислительной техники.\n"
					"По сути, в 21 веке ни одна отрасль не обходится без специалистов IT-сферы, так как информационные технологии внедряются везде, по той причине, что автоматизация приносит качественные изменения.")
			elif msg == "тарифы":
				sender9(id,"Вот Тарифы")
			elif msg == "low":
				sender9(id,"Составление программы развития на 2-3 месяца - 450 руб.")
			elif msg == "lowmax":
				sender9(id,"Составление программы развития на 2-3 месяца, помощь в изучении - 1350 руб.")
			elif msg == "medium":
				sender9(id,"Составление программы развития на 5-6 месяцов - 700 руб.")
			elif msg == "mediummax":
				sender9(id,"Составление программы развития на 5-6 месяцов, помощь в изучении - 2100 руб.")
			elif msg == "lowpromax":
				sender9(id,"Составление основной программы и общей программы развития на 2-3 месяца - 650 руб.")
			elif msg == "mediumpromax":
				sender9(id,"Составление основной программы и общей программы развития на 5-6 месяцов - 1100 руб.")
			elif msg == "high":
				sender9(id,"Составление основной программы и общей программы развития, помощь в изучении на 2-3 месяца - 2100 руб.")
			elif msg == "highmax":
				sender9(id,"Составление основной программы и общей программы развития, помощь в изучении на 5-6 месяцов - 3600 руб.")
			else:
				sender7(id,"Извините, я вас не понял, отвечайте корректнее!")