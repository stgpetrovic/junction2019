function perc2color(perc) {
	var r, g, b = 0;
	if(perc < 50) {
		r = 255;
		g = Math.round(5.1 * perc);
	}
	else {
		g = 255;
		r = Math.round(510 - 5.10 * perc);
	}
	var h = r * 0x10000 + g * 0x100 + b * 0x1;
	return '#' + ('000000' + h.toString(16)).slice(-6);
}

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
        this.filledBar.style.width = `${x}%`;
        this.filledBar.style.backgroundColor = perc2color(x);
    }
};

class Popup {
    constructor(name) {
        this.text = '';
        this.name = name;
        this.popupDiv = document.createElement('div');
        this.popupText = document.createElement('p');
        this.popupImage = document.createElement('img');
        this._init();
    }

    attach(heading) {
        heading.appendChild(this.popupDiv);
    }

    _init() {
        this._initPopupText();
        this.popupDiv.appendChild(this.popupText);
        this.popupDiv.appendChild(this.popupImage);
    }

    _initPopupText() {
        this.popupText.className += " green-basket-popup-text";
        this.popupText.style.position = "relative";
        this.popupText.style.padding = "15px";
        this.popupText.style.border = "5px solid #5a8f00";
        this.popupText.style.color = "#333";
        this.popupText.style.background = "#fff";
        this.popupText.style.border_radius = "10px";
        this.setText('Test text');
    }

    setText(txt) {
        if(txt.length == 0) {
            console.log('Removing popup text.');
            this.popupText.style.display = "none";
        } else {
            console.log(`Setting the popup text to ${txt}`);
            this.popupText.innerText = txt;
            this.popupText.style.display = "block";
        }
    }

    decideDisplay(score, suggest) {
        if(score >= 70) {
            this.setText('Good job!');
            this.popupImage.style.display = "none";
            return;
        }
        this.setText(suggest.target.name);
        this.popupImage.style.display = "block";
        this.popupImage.src = suggest.target.pic_url;
    }
};

function insertElement() {
    var heading = document.getElementsByClassName("shopping-list-heading")[0];
    var div = document.createElement('div');
    div.style.display = "none";
    heading.appendChild(div);

    var healthyBar = new Bar("Health score");
    healthyBar.attach(div);

    var greenBar = new Bar("Green score");
    greenBar.attach(div);

    var popup = new Popup("Substitute popup");
    popup.attach(div);

    return {
        div,
        healthyBar,
        greenBar,
        popup
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

    var jsCheckBasket = setInterval(checkBasket, 1031);

    function checkBasket() {
        var cart = getCart();
        if (cart.length === 0) {
            hideBars();
        } else {
            showBars();
        }
        fetch(
            "http://127.0.0.1:5000/goodness",
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
        .then(json => {
            widget.healthyBar.setFill(json.score);
            widget.popup.decideDisplay(json.score, json.suggest);
            widget.greenBar.setFill(json.sustainable);
        })
        .catch(reason => console.log(reason));
    }

    function hideBars() {
        document.getElementsByClassName("shopping-list-content")[0].style.paddingTop = "70px";
        widget.div.style.display = "none";
    }

    function showBars() {
        document.getElementsByClassName("shopping-list-content")[0].style.paddingTop = "272px";
        widget.div.style.display = "block";
    }
}
