for client in range(1, 4):
    name = input(f"Donner le nom et prénom du client n{client} : ")
    n = int(input(f"Donner le nombre darticles pour le client n{client} : "))

    price_before_tax = 0

    for article in range(1, n + 1):
        s = float(input(f"Donner le prix de larticle {article} : "))
        price_before_tax += s

    ttc = price_before_tax + (price_before_tax * 0.15) - (price_before_tax * 0.02)

    print(f"Le Total à payer pour le client {name} est : {ttc:.2f} DH")
