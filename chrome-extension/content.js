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
        this.popupImageSrc = document.createElement('img');
        this.popupImageSrc.className = "recommendation-target-image";
        this.popupImageArrow = document.createElement('p');
        this.popupImageArrow.className = "recommendation-target-arrow";
        this.popupImageArrow.innerText = '🠆';
        this.popupImageDst = document.createElement('img');
        this.popupImageDst.className = "recommendation-target-image";
        this._init();
    }

    attach(heading) {
        heading.appendChild(this.popupDiv);
    }

    _init() {
        this._initPopupText();
	this._initPopupDiv();
        this.popupDiv.appendChild(this.popupText);
        this.popupDiv.appendChild(this.popupImageSrc);
        this.popupDiv.appendChild(this.popupImageArrow);
        this.popupDiv.appendChild(this.popupImageDst);
    }

    _initPopupText() {
        this.popupText.className += " green-basket-popup-text";
        this.setText('Test text');
    }

    _initPopupDiv() {
        this.popupDiv.className += " green-basket-popup-div";
    }

    setText(txt) {
        if(txt.length == 0) {
            // console.log('Removing popup text.');
            this.popupText.style.display = "none";
        } else {
            // console.log(`Setting the popup text to ${txt}`);
            this.popupText.innerText = txt;
            this.popupText.style.display = "block";
        }
    }

    decideDisplay(score, suggest) {
        if(!suggest || !suggest.target) {
            this.setText('Good job!');
            this.popupDiv.style.display = "none";
            this.popupImageSrc.style.display = "none";
            this.popupImageArrow.style.display = "none";
            this.popupImageArrow.style.onclick = "";
            this.popupImageDst.style.display = "none";
            return;
        }
        this.setText('Swap ' + suggest.source.name + ' for ' + suggest.target.name);
        this.popupDiv.style.display = "block";
        this.popupImageSrc.style.display = "inline-block";
        this.popupImageSrc.src = suggest.source.pic_url;
        this.popupImageArrow.style.display = "inline-block";
        this.popupImageArrow.onclick = function() {substituteSuggestion(suggest.source.ean, suggest.target.ean);};
        this.popupImageDst.style.display = "inline-block";
        this.popupImageDst.src = suggest.target.pic_url;
    }
};

class BasketLogo {
    constructor() {
        this.container = document.createElement('div');
        this.container.className = "green-basket-logo";
        this.svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        this.container.appendChild(this.svg);
        this.tooltip = document.createElement('span');
        this.tooltip.className = "green-basket-hidden-tooltip";
        this.container.appendChild(this.tooltip);
        this._init();
    }

    attach(div) {
        div.appendChild(this.container);
    }

    setTooltipText(tooltip) {
        if (!tooltip) {
            this.tooltip.className = "green-basket-hidden-tooltip"
            this.svg.style.animation = "";
        } else {
            this.tooltip.className = "green-basket-tooltip";
            this.tooltip.innerText = tooltip;
            this.svg.style.animation = "logoGlow 4s infinite";
        }
    }

    update(logo) {
        this._updatePart(this.basket, logo.basket);
        this._updatePart(this.eyes, logo.eyes);
        this._updatePart(this.mouth, logo.mouth);
    }

    _init() {
        var ns = 'http://www.w3.org/2000/svg'
        this.svg.setAttributeNS(null, 'width', '100');
        this.svg.setAttributeNS(null, 'height', '100');
        this.svg.setAttributeNS(null, 'viewBox', '0 0 300 300');
        this.svg.setAttribute(null, 'xmlns', "http://www.w3.org/2000/svg");
        this.svg.setAttributeNS("http://www.w3.org/2000/svg", 'xlink', "http://www.w3.org/1999/xlink");

        this.basket = this._createPart(this.svg);
        this.eyes = this._createPart(this.svg);
        this.mouth = this._createPart(this.svg);
    }

    _createPart() {
        var ns = 'http://www.w3.org/2000/svg'
        var image = document.createElementNS(ns, "image");
        this.svg.appendChild(image);
        return image;
    }

    _updatePart(image, part) {
        image.setAttributeNS(null, "height", part["height"]);
        image.setAttributeNS(null, "width", part["width"]);
        image.setAttributeNS(null, "x", part["x"]);
        image.setAttributeNS(null, "y", part["y"]);
        image.setAttributeNS("http://www.w3.org/1999/xlink", "href", chrome.runtime.getURL(part["href"]));
    }
};

function insertElement() {
    var content = document.getElementsByClassName("shopping-list-content")[0];
    var child = content.getElementsByClassName("shopping-list-shopping-content")[0];
    var div = document.createElement('div');
    div.style.display = "none";
    content.insertBefore(div, child);

    var basketLogo = new BasketLogo();
    basketLogo.attach(div);

    var bars = document.createElement('div');
    bars.className = "green-basket-bars";
    div.appendChild(bars);

    var healthyBar = new Bar("Health score");
    healthyBar.attach(bars);

    var greenBar = new Bar("Green score");
    greenBar.attach(bars);

    var popup = new Popup("Substitute popup");
    popup.attach(div);

    return {
        div,
        healthyBar,
        greenBar,
        popup,
        basketLogo,
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

var session_id = '';
var session_id_regex = /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/g;

function getSessionId() {
  if(session_id.length != 0) {
    return session_id;
  }

  requests = window.performance.getEntries().filter(e=>e.initiatorType==='xmlhttprequest');
  for([index, request] of Object.entries(requests)){
    matches = request.name.match(session_id_regex);
    if(matches != null && matches.length >= 1) {
      session_id = matches[0];
      session_id_found = true;
      console.log('Session id found!');
      return session_id;
    }
  }
  console.log('Session id not found!');
  return '';
}

async function updateAmounts(ean, count) {
  session_id = getSessionId();
  if(session_id.length == 0) {
    console.log('Cuould not update an item due to a missing session id.');
    return;
  }
  url = 'https://www.k-ruoka.fi/kr-api/order-drafts/' + session_id + '/update?storeId=N106';
  data = [{"type":"ITEM","id":ean,"ean":ean,"amountInfo":{"amount":count,"unit":"kpl"},"allowSubstitutes":true}];
  try {
    response = await fetch(url, {
      method: 'PUT',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }});
      json = await response.json();
        console.log('Success:', JSON.stringify(json));
      } catch (error) {
        console.error('Error:', error);
      }
}

async function removeItem(ean) {
  session_id = getSessionId();
  if(session_id.length == 0) {
    console.log('Cuould not remove an item due to a missing session id.');
    return;
  }
  url = 'https://www.k-ruoka.fi/kr-api/order-drafts/' + session_id + '/update?storeId=N106';
  data = [{"type":"REMOVE","itemId":ean}];
  try {
    response = await fetch(url, {
      method: 'PUT',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }});
      json = await response.json();
        console.log('Success:', JSON.stringify(json));
      } catch (error) {
        console.error('Error:', error);
      }
}

async function updateCart(eans_counts) {
  session_id = getSessionId();
  if(session_id.length == 0) {
    console.log('Cuould not update cart due to a missing session id.');
    return;
  }
  url = 'https://www.k-ruoka.fi/kr-api/order-drafts/' + session_id + '/update?storeId=N106';
  data = [];
  for([index, ean_count] of Object.entries(eans_counts)){
    if(ean_count.count == 0) {
      data.push({"type":"REMOVE","itemId":ean_count.ean});
    } else {
      data.push({"type":"ITEM","id":ean_count.ean,"ean":ean_count.ean,"amountInfo":{"amount":ean_count.count,"unit":"kpl"},"allowSubstitutes":true});
    }
  }
  try {
    response = await fetch(url, {
      method: 'PUT',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }});
      json = await response.json();
        console.log('Success:', JSON.stringify(json));
      } catch (error) {
        console.error('Error:', error);
      }
}

function substituteSuggestion(source_ean, target_ean) {
  cart = getCart();
  var source_count = 1;
  for([index, item] of Object.entries(cart)) {
    if(item.ean == source_ean) {
      source_count = item.amount.amount;
    }
  }
  updateCart([{ean: source_ean, count: 0},
              {ean: target_ean, count: source_count}]);
  window.location.reload(false); 
  // removeItem(source_ean);
  // updateAmounts(target_ean, source_count);
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

    var jsCheckBasket = setInterval(checkBasket, 1033);

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
            widget.basketLogo.update(json.logo);
            widget.basketLogo.setTooltipText(json.shipit);
        })
        .catch(reason => console.log(reason));
    }

    function hideBars() {
        widget.div.style.display = "none";
    }

    function showBars() {
        widget.div.style.display = "block";
    }
}
