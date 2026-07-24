from receipt import generate_receipt

bill = [

    {
        "name":"Coke",
        "quantity":2,
        "price":40,
        "total":80
    },

    {
        "name":"Maggi",
        "quantity":3,
        "price":20,
        "total":60
    },

    {
        "name":"Lays",
        "quantity":1,
        "price":20,
        "total":20
    }

]

generate_receipt(bill,160)