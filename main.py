import discord
import tensorflow as tf

client = discord.Client()

@client.event
async def on_ready():
    print("봇 구동 중")
    bar = discord.Game("최적의 값 계산")
    await client.change_presence(status=discord.Status.online, activity=bar)

key = 0
shoes = 0
sta_hour = 0
sta_min = 0
end_hour = 0
end_min = 0
test1 = 2
test2 = 7
test3 = 10
a = tf.Variable(0.1)
b = tf.Variable(0.2)
c = tf.Variable(0.1)
d = tf.Variable(0.2)
e = tf.Variable(0.1)
f = tf.Variable(0.1)

def loss():
    predict = key * a + b
    return tf.square(shoes - predict)

def loss2():
    predict = sta_min * c + d
    return tf.square(end_min - predict)

def loss3():
    predict = test1 * e + f
    return tf.square(test2 - predict)

opt = tf.keras.optimizers.Adam(learning_rate = 0.1)
for i in range(1000):
    opt.minimize(loss3, var_list=[e,f])
print("`a = " + str(e.numpy()) + " b = " + str(f.numpy()) + "`")

print(str(test3 * e + f))

@client.event
async def on_message(message):
    global key, shoes, a, b, sta_hour, sta_min, end_hour, end_min
    if message.content.startswith("!키를 이용한 신발사이즈를 구하는 딥러닝 시스템"):
        key = float(message.content[27:30])
        shoes = float(message.content[31:34])
        opt = tf.keras.optimizers.Adam(learning_rate = 0.1)
        for i in range(150):
            opt.minimize(loss, var_list=[a,b])
            await message.channel.send("`a = " + str(a.numpy()) + " b = " + str(b.numpy()) + "`")
        await message.channel.send("`입력된 신발 사이즈 : " + str(shoes) + " 딥러닝 결과 사이즈 : " + str(key * a.numpy() + b.numpy()) + " 오차 : " + str(shoes - (key * a.numpy() + b.numpy())) + "`")

    if message.content.startswith("!키입력"):
        key = int(message.content[5:])
        await message.channel.send("`" + str(key * a + b) + "`")

    if message.content.startswith("!학교 도착시간 데이터 학습"):
        sta_hour = float(message.content[16:17])
        sta_min = float(message.content[18:20])
        end_hour = float(message.content[21:22])
        end_min = float(message.content[23:25])
        opt = tf.keras.optimizers.Adam(learning_rate = 0.1)
        for i in range(150):
            opt.minimize(loss2, var_list=[c,d])
            await message.channel.send("`a = " + str(c.numpy()) + " b = " + str(d.numpy()) + "`")
        await message.channel.send("`입력된 도착시간 : " + str(end_hour) + "시 " + str(end_min) + "분 딥러닝 결과 도착시간 : " + str(end_hour) + "시 " + str(sta_min * c.numpy() + d.numpy()) + "분 오차 : " + str(end_min - (sta_min * c.numpy() + d.numpy())) + "분`")

    if message.content.startswith("!출발시간 입력"):
        sta_hour = float(message.content[9:10])
        sta_min = float(message.content[11:13])
        await message.channel.send("`" + "예상 도착시간 : 7시 " + str(int(sta_min * c.numpy() + d.numpy()) - 1) + "분 ~ 7시 " + str(int(sta_min * c.numpy() + d.numpy()) + 1) + "분`")

client.run("OTA3OTk3NDcwMzQ3Mzc4Njk4.YYvUig.TSdYCXPi8eRTQWwZ_BtVygg63xU")