from shoppingcart import Cart

cart = Cart()

cart.tambahProduk("mangga", 1)
cart.tambahProduk("apel", 2)
cart.tambahProduk("jeruk", 3)

cart.hapusProduk("apel")

cart.tampilkanCart()
