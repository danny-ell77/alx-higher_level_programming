#!/usr/bin/node
module.exports = class Rectangle {
    constructor(w, h) {
        if (w > 0  && h > 0) {
            this.width = w;
            this.height = h;
        }
    }
    
    print() { 
        var some_string = ""
        for (let h = this.height; h > 0; h--) { 
            for (let w = this.width; w > 0 ; w--) { 
                some_string += "X";
            }
            console.log(some_string)
            some_string = "";
        }
    }

    rotate() { 
        const tmp = this.width
        this.width = this.height
        this.height = tmp
    }

    double() { 
        this.width *= 2
        this.height *= 2
    }
}
