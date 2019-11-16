class Bar {
    constructor(name) {
        this.filled_percent = 0;
        this.name = name;
        this.barContainer = document.createElement('div');
        this.barName = document.createElement('div');
        this.fullBar = document.createElement('div');
        this.filledBar = document.createElement('div');
        this._init();
    }

    attach(heading) {
        heading.appendChild(this.barContainer);
    }

    _init() {
        this._initBarContainer();
        this._initBarName();
        this._initFullBar();
        this._initFilledBar();
        this.barContainer.appendChild(this.barName);
        this.barContainer.appendChild(this.fullBar);
        this.fullBar.appendChild(this.filledBar);
    }

    _initBarContainer() {
        this.barContainer.className += " green-basket-bar-container";
    }

    _initBarName() {
        this.barName.innerText = this.name;
        this.barName.className += " green-basket-bar-name";
    }

    _initFullBar() {
        this.fullBar.style.width = "100%";
        this.fullBar.style.backgroundColor = "#ddd";
    }

    _initFilledBar() {
        this.filledBar.style.width = "0%";
        this.filledBar.style.height = "30px";
        this.filledBar.style.backgroundColor = "#4CAF50";
        this.filledBar.style.textAlign = "center";
        this.filledBar.style.lineHeight = "30px";
        this.filledBar.style.color = "white";
    }

    setFill(x) {
        console.log(`Setting the width to ${x}`);
        this.filledBar.style.width = `${x}%`;
    }
};

function insertElement() {
    var heading = document.getElementsByClassName("shopping-list-heading")[0];
    var div = document.createElement('div');
    heading.appendChild(div);

    var healthyBar = new Bar("Health score");
    healthyBar.attach(div);

    var greenBar = new Bar("Green score");
    greenBar.attach(div);
    return {
        div,
        healthyBar,
        greenBar
    };
}

window.addEventListener ("load", main, false);

function getCart() {
    var items = document.getElementsByClassName("shopping-list-item");
    var shoppingIds = [];
    for (var i = 0; i < items.length; ++i) {
        var item = items[i];
        shoppingIds.push({
            "ean": item.id.split("-").slice(-1)[0],
            "amount": getAmounts(item),
        });
    }
    return shoppingIds;
}

function getAmounts(item) {
    var container = item.getElementsByClassName("product-shopping-list-amount-container")[0];
    var amount = container.getElementsByClassName("amount")[0].innerText.trim();
    var pricingUnit = container.getElementsByClassName("pricing-unit")[0].innerText.trim();
    return {
        amount,
        pricingUnit,
    };
}

function main() {
    var widget;
    var jsInitChecktimer = setInterval(checkForJS_Finish, 111);

    function checkForJS_Finish() {
        if (document.getElementsByClassName("shopping-list-heading")) {
            clearInterval(jsInitChecktimer);
            widget = insertElement();
        }
    }

    var jsCheckBasket = setInterval(checkBasket, 2000);

    function checkBasket() {
        var cart = getCart();
        fetch(
            "http://127.0.0.1:5000/goodness/",
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                  },
                  method: "POST",
                  body: JSON.stringify({
                      "eans": cart.map(item => item.ean)
                  }),
            },
        )
        .then(response => response.json())
        .then(json => widget.healthyBar.setFill(json.score))
        .catch(reason => console.log(reason));
    }
}
