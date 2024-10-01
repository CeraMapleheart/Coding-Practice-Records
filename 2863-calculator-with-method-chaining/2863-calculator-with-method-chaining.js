class Calculator {
    constructor(value = 0) {
        this.value = value;
    }

    add(num) {
        this.value += num;
        return this;
    }

    subtract(num) {
        this.value -= num;
        return this;
    }

    multiply(num) {
        this.value *= num;
        return this;
    }

    divide(num) {
        if (num !== 0) {
            this.value /= num;
        }
        else {
            throw new Error("Division by zero is not allowed");
        }
        return this;
    }

    power(num) {
        this.value = Math.pow(this.value,num);
        return this;
    }

    getResult() {
        return this.value;
    }
}
