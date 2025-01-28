# #MATRIZ ES UNA LISTA COMPUESTA POR LISTAS

# m=[
#     [
#         [2,7,5],
#     [3,4,7,15]
#     ],
    
#     [
#     [9,1,2],
#     [8,6,71]
#     ]
#    ]

# print(m[1][1][0])

# # for f in m:
# #     print(f)

d = {"nombre": "Cesar Huispe", 
	"fonos": [
			988778882, 
			988877776, 
			877666333], 
	"activo": True}
product={
    "uva": 1400,
    "pera":1200,
    "melon": 1000,
    "verduras":{"papa": 600, "pepino": 500}
    
}
# print(product)

for clave, valor  in product.items():
    print(f"{clave} = ${valor}")