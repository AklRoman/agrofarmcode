import os
from datetime import datetime
import logging
import threading
import paho.mqtt.client as mqtt
import serial
import time

"""
ser = serial.Serial('COMx', 115200)  
temperature = None
humidity = None
water_level = None


def send_command(command):
    ser.write(command.encode())


def esp32_message_handler():
    global temperature, humidity, water_level
    while True:
        data = ser.readline().decode().strip()
        if data.startswith("Temperature:"):
            temperature = data.replace("Temperature:", "").strip()
            print("Temperature:", temperature)
        elif data.startswith("Humidity:"):
            humidity = data.replace("Humidity:", "").strip()
            print("Humidity:", humidity)
        elif data.startswith("Water level:"):
            water_level = data.replace("Water level:", "").strip()
            print("Water level:", water_level)
        time.sleep(1)


esp32_thread = threading.Thread(target=esp32_message_handler)
esp32_thread.start()"""

farm_number = 'rhf8ayDwMXeIO3VNroIg7FAHU'
logging.basicConfig(level=logging.DEBUG)

plants = ("Морковь", "Свёкла", "Редис", "Петрушка", "Кинза", "Чеснок", "Зеленый лук", "Сельдерей", "Репа", "Капуста",
          "Салат латук", "Руккола", "Базилик", "Укроп", "Шпинат")

isPlantInProgress = None
start_time = None


def morkov(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def svekla(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def redis(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def petrushka(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def kinza(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def chesnok(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def zeleniy_luk(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def selderey(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def repa(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def kapusta(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def salat_latuk(client_id, plant):
    global isPlantInProgress, polivki_salat, pahaniya_salat
    polivki_salat = 2
    pahaniya_salat = 1
    with open("plantProgressTemp.txt", "a") as progress:
        isPlantInProgress = plant
        progress.write(f"{plant}_planted\n")
        time.sleep(10)
        while polivki_salat > 0 or pahaniya_salat > 0:
            if polivki_salat > 0:
                progress.write(f"watered\n")
                polivki_salat -= 1
            time.sleep(10)
            if pahaniya_salat > 0:
                progress.write(f"razrihlen\n")
                pahaniya_salat -= 1
            time.sleep(10)
        progress.write(f"Готово\n")
        # print("Файл прогресса был очищен")
        isPlantInProgress = None
        mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def rukkola(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def bazilik(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def ukrop(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


def shpinat(client_id, plant):
    global isPlantInProgress
    isPlantInProgress = plant
    time.sleep(15)
    isPlantInProgress = None
    mqttc.publish("agro_farm", f"{client_id}ready {plant}")


plantFuncDict = {
    "Морковь": morkov,
    "Свёкла": svekla,
    "Редис": redis,
    "Петрушка": petrushka,
    "Кинза": kinza,
    "Чеснок": chesnok,
    "Зеленый лук": zeleniy_luk,
    "Сельдерей": selderey,
    "Репа": repa,
    "Капуста": kapusta,
    "Салат латук": salat_latuk,
    "Руккола": rukkola,
    "Базилик": bazilik,
    "Укроп": ukrop,
    "Шпинат": shpinat
}
mqttc = mqtt.Client()


def handle_message(client, userdata, message):
    msg = message.payload.decode("utf-8")
    if "getStatus" in msg:
        logging.info("[RASPBERRY MESSAGE] Получено сообщение getStatus")
        client_id, shit = msg.split("getStatus", 1)
        status = getStatus()
        mqttc.publish("agro_farm", f"{client_id}{status}")
        logging.info("[RASPBERRY MESSAGE] Отправлен статус")
    if "plant: " in msg:
        logging.info("[RASPBERRY MESSAGE] Получено сообщение plant")
        msg = msg.replace("plant:", "")
        client_id, plant = msg.split(' ', 1)
        if isPlantInProgress is not None:
            mqttc.publish("agro_farm", f"{client_id} alreadplanting {isPlantInProgress}")
        else:
            logging.info(f"[RASPBERRY MESSAGE] Полученное растение: {plant} от {client_id}")
            time.sleep(1)
            run_func(plant, client_id)


def plant_publish(client_id, plant):
    mqttc.publish("agro_farm", f"{client_id}planted {plant}")


def run_func(plant, client_id):
    """global start_time"""
    plant_thread = threading.Thread(target=plantFuncDict[plant], args=(client_id, plant))
    plant_thread.start()
    """start_time = datetime.now()"""


def restore_progress():
    with open("plantProgressTemp.txt", "r") as progress:
        lines = progress.readlines()
        try:
            if lines:
                last_line = lines[-1]
                if last_line.strip() == "Ready":
                    return None
                else:
                    parts = last_line.strip().split("_planted")
                    if len(parts) == 2:
                        return parts
        except:
            pass


def on_connect(client, userdata, flags, rc):
    global pahaniya_salat, polivki_salat
    if rc == 0:
        print("MQTT подключен")
        logging.info("MQTT для RASPBERRY подключен")
        client.subscribe("agro_bot")
        # Восстановление прогресса после перезапуска
        restored_progress = restore_progress()
        if restored_progress:
            restored_plant, actions = restored_progress
            print(restored_plant, actions)
    else:
        print("Failed to connect, return code: ", rc)
        logging.warning("MQTT для RASPBERRY НЕ подключен")


"""def plantedTime():
    global start_time
    current_time = datetime.now()
    if isPlantInProgress is not None:
        difference = current_time - start_time
    else:
        difference = 0
    return difference"""


def getStatus():
    waterStatus = getWaterStatus()
    earthStatus = getEarthStatus()
    airStatus = getAirStatus()
    status = f"Растение: {isPlantInProgress}\n" \
             f"Вода: {waterStatus}\n" \
             f"Земля: {earthStatus}\n" \
             f"Воздух: {airStatus} MOCKUP"
    return status


def getWaterStatus():
    waterAmount = 79
    waterStatus = f"воды в баке : {waterAmount}%"
    return waterStatus


def getEarthStatus():
    humidity = 30
    age = 12
    earthStatus = f"влажность почвы: {humidity}%, возраст почвы: {age} дней"
    return earthStatus


def getAirStatus():
    temperature = 22
    waterStatus = f"температура воздуха: {temperature} градусов"
    return waterStatus


mqtt_username = "agro"
mqtt_password = "faU28gaK"


mqttc.on_connect = on_connect
mqttc.on_message = handle_message

# Set MQTT username and password
mqttc.username_pw_set(mqtt_username, mqtt_password)
mqttc.connect("11.165.169.20", 8883, 60)

mqtt_thread = threading.Thread(target=mqttc.loop_forever)
mqtt_thread.start()
