# L0_early_user_checker
Проверяет кошельки на сайте https://dune.com/0xtoshi/layerzero-early-and-druable-user-fees-spent

Рядом с main или exe должен лежать wallets.txt в который нужно записать все адреса кошельков для проверки. По одному кошельку в каждой строке.

<span style="background-color: red; color: white;">Красный (critical)</span> - нет на сайте  
<span style="color: red;">Красный</span> - есть на сайте, но нет никаких галочек  
<span style="color: blue;">Синий</span> - только галочка durable_user  
<span style="color: yellow;">Желтый</span> - только галочка early_user  
<span style="color: green;">Зеленый</span> - обе галочки