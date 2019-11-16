class GreenBar {
    constructor() {
        this.filled_percent = 0;
        this.barContainer = document.createElement('div');
        this.fullBar = document.createElement('div');
        this.filledBar = document.createElement('div');
        this._init();
    }

    attach(heading) {
        heading.appendChild(this.barContainer);
    }

    _init() {
        this._initFullBar();
        this._initFilledBar();
        this.barContainer.appendChild(this.fullBar);
        this.fullBar.appendChild(this.filledBar);
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

    var healthyBar = new GreenBar();
    healthyBar.attach(div);
    return {
        div,
        healthyBar
    };
}

window.addEventListener ("load", main, false);

function getAllShoppingIds() {
    var items = document.getElementsByClassName("shopping-list-item");
    var shoppingIds = [];
    for (var i = 0; i < items.length; ++i) {
        shoppingIds.push(items[i].id.split("-").slice(-1)[0]);
    }
    return shoppingIds;
}

function main() {
    var jsInitChecktimer = setInterval(checkForJS_Finish, 111);
    var widget;

    function checkForJS_Finish () {
        if (document.getElementsByClassName("shopping-list-heading")) {
            clearInterval(jsInitChecktimer);
            widget = insertElement();
        }
    }

    var jsCheckBasket = setInterval(checkBasket, 222);

    function checkBasket() {
        var ids = getAllShoppingIds();
        console.log("Basket: ", getAllShoppingIds());
        widget.healthyBar.setFill(ids.length * 10);
    }
}
