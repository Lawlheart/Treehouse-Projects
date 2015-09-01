var calculator = {
		sum: 0,
		add: function(value) {
			this.sum += value
    },
    subtract: function(value) {
    	this.sum -= value
    },
    multiply: function(value) {
    	this.sum *= value
    },
    divide: function(value) {
    	this.sum /= value
    },
    clear: function() {
    	this.sum = 0
    }, 
    equals: function() {
    	return this.sum
    }
}
calculator.add(1)
calculator.add(2)
calculator.add(3)
console.log(calculator.equals())