# My Condition Codes (Seperate from the codes from OpenWeatherMap)

| condition | condition_code | OpenWeatherMap data |
|-----------|:--------------:|--------------------:|
chilly | 1 | > Tmp > 40F && < 60F
cold | 2 | Tmp < 40F
hot | 3 | Tmp > 80F < 95F
neutral | 4 | Tmp < 80F > 60F
rain | 5 | weather_id > 500 && < 600
snow | 6 | weather_id > 600 && < 700
windy | 7 | wind_speed > 20mph

Priority List
1. Snow
2. Rain
3. Windy
4. Temperature conditions
