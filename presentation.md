Hello!

[Load the page]

We are team green basket and we have created a socially responsible... artificial intelligence...
smart shoppig assistent. A socially responisble, artificial intelligence smart shopping assistant.

[Add a good item to the cart].

Meet Baskey the Green Basket. [Mouse pointer circles Baskey]. Baskey tells you how healthy and
sustainble your current basket selection is.

[Add a bad item for sustainability to the cart]

When you make a bad choice, Baskey's personality shines through, and hus avatar provides immediate
feedback about how he feels about your choice.

[Hover over Baskey]

Baskey is also a teacher - he glows when he has something to say that explains how you can make
better choices in the future.

[Click the swap button]

Not only that, he allows you to easily make a better choice by providing you with better
alternatives.

[Keep running the demo at your leisure - add the second bad item, this time health, focused.
Replace it when ready.]

We have used machine learning algorithms to train Baskey on the receipt data provided to us by
Kesko. We started with a multivariate linear regression model that we used to bootstrap early
iterations of Baskeys brains, and that we used to find tricky cases. We improved our machine
learning algoirthm's quality by building a simple app that allowed a human operator to pick the
better of the two choices and used that to build a high signal, robust training set.

[Go on stage with the app]

But wait, that's not all. We also built an artificial reality Android app that brings Baskey into
your pocket.

[Scan a barcode]

The app allows you to scan any barcode and Baskeys familar face will immediately tell you how he
feels about your choice.


OLD:


smart shopping assistant that gives you instant
feedback about the items that you're adding to your shopping cart. As you keep placing more and
more items into the cart, Baskey the Green Basket immediately tells you how healthy and sustainable
your basket is. What's more, he helps you learn what you can do to improve both the healtiness and
the susistainability of your shopping habbits by offering context sensitive tips and like-for-like
suggestions for the products you have suggested.

We have used the data provided by the Kesko API to build our health and sustainibity models. We
first started with a simple multivariate linear regression model that looked at the ingredients
and tried to calculate how healty or sustainble an option is. This model was used to iterate on the
initial implementation and later served for finding interesting cases for more sophisticated
approaches. We've built a helper application that allowed us to classify those cases manually, by
presenting us two options and a human operator had to decide which one is healthier.
Using this app and the free cycles we've had during the hackathon, we have acquired a high quality,
robust training set that we then used to train the machine learning model for the recommendation
engine. The final model takes into account a multitude of features, from the nutrient information,
country of origin, to the user bucket information provided through the receipt history API.

Oh, but that's not all. We've also made an Android app to brink Baskey to life in the real world,
via augmented reality. You just need to scan the barcode of the item, and Basky will immediately
tell you what he thinks of it.


Demo flow:

1. Open the web page.
2. Add a good item to the basket.
3. Add a bad, far away item to the basket. It should trigger ship it.
4. Show the ship it suggestion.
5. Click swap to execute the swap.

Izlike:
- Lose je osvjetljenje pa citac barkoda nije stabilan.
