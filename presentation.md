Hello!

We are team green basket and we have created a smart shopping assistant that gives you instant
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
