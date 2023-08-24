import folium
from folium.vector_layers import PolyLine
def calculate_distance(point1, point2):
   
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2-x1)**2+(y2-y1)**2)**1/2
    return distance
# Поиск наиболее подходящих заказов по пути маршрута водителя
def find_suitable_orders(driver_route, orders):

    driver_start, driver_end = driver_route
    suitable_orders = []
    total_distance = calculate_distance(driver_start, driver_end)
    for order in orders:
        order_start, order_end, order_color = order['начало'], order['конец'], order['цвет']
        distance_to_start = calculate_distance(driver_start, order_start)
        distance_to_end = calculate_distance(driver_end, order_end)
        
        print("\n","distance_to_start",distance_to_start,"\n",
              "distance_to_end",distance_to_end,"\n",
              "total_distance",total_distance,"\n",
              "order",order, "\n",
              "order_color",order_color,"\n")
            
        if (distance_to_start + distance_to_end) < total_distance:
            suitable_orders.append(order)
    return suitable_orders

# Пример маршрута водителя в Якутске
driver_route = [(62.003483, 129.700936), (62.103304, 129.757543)] 
# Общий заказ 
orders = [
    {
        'начало': [62.023816, 129.727324],
        'конец': [62.049145, 129.747004],
        'цвет': 'blue'
    },
    {
        'начало': [62.0281, 129.7326],
        'конец': [62.036254, 129.66019],
        'цвет': 'green'
    },
    {
        'начало': [62.027, 129.733],
        'конец': [62.0059, 129.671531],
        'цвет': 'purple'
    },
    {
        'начало': [62.023038, 129.71421],
        'конец': [62.013244, 129.718212],
        'цвет': 'purple'
    }
]

suitable_orders = find_suitable_orders(driver_route, orders)

print("Наиболее подходящие заказы по пути маршрута водителя:")
for order in suitable_orders:
    print(order) 
print("-------------------------")


# Координаты Якутска
latitude, longitude = 62.0355, 129.6759
# Начало таксиста
marker_coords_start = 62.003483, 129.700936
# Конец таксиста
marker_coords_end = 62.103304, 129.757543
# Создание карты




map = folium.Map(location=[latitude, longitude], zoom_start=10)

# Путь таксиста 
folium.Marker(location=marker_coords_start, popup='начало', icon=folium.Icon(color='red')).add_to(map)
folium.Marker(location=marker_coords_end, popup='конец', icon=folium.Icon(color='red')).add_to(map)
folium.PolyLine([marker_coords_start, marker_coords_end], color='red').add_to(map)



for order in orders:
    folium.Marker(location=order['начало'], popup=f"заказ_{order['цвет']}_начало", icon=folium.Icon(color=order['цвет'])).add_to(map)
    folium.Marker(location=order['конец'], popup=f"заказ_{order['цвет']}_конец", icon=folium.Icon(color=order['цвет'])).add_to(map)
    folium.PolyLine([order['начало'], order['конец']], color=order['цвет']).add_to(map)


# Вывод карты на экран
map.save('map.html')    