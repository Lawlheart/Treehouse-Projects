//Problem: user interaction doesn't produce desired results
//Solution: add interactivity so the user can manage daily tasks
//notes: it looks like the form elements aren't id-ed, so we're probably going to need to use relative object properties - i.e. traversal - to get the desired results

var taskInput = document.getElementById('new-task'); //$('#new-task')
var addButton = document.getElementById('add-button');//$('#add-button')
var incompleteTasksHolder = document.getElementById('incomplete-tasks'); //$('#incomplete-tasks')
var completeTasksHolder = document.getElementById('completed-tasks'); //$('#completed-tasks')

//New Task List Item
var createNewTaskElement = function(taskString) {
	//create list item
	var listItem = document.createElement('li');
	//input (checkbox)
	var checkBox = document.createElement('input');
	checkBox.type = "checkbox"
	//label
	var label = document.createElement('label');
	label.innerHTML = taskString;
	//input (text)
	var input = document.createElement('input');
	input.type = "text"
	//button.edit
	var editButton = document.createElement('button');
	editButton.innerHTML = 'Edit';
	editButton.className = 'edit';
	//button.delete
	var deleteButton = document.createElement('button');
	deleteButton.innerHTML = 'Delete';
	deleteButton.className = 'delete';
	//each elements, needs modified and appended
	listItem.appendChild(checkBox);
	listItem.appendChild(label);
	listItem.appendChild(input);
	listItem.appendChild(editButton);
	listItem.appendChild(deleteButton);
	return listItem
}

//add a new task
var addTask = function() {
	console.log('Add Task...')
	//create a new list item with the text from the new task
	var listItem = createNewTaskElement(taskInput.value)
	taskInput.value="";
	//append listItem to incompleteTasksHolder
	incompleteTasksHolder.appendChild(listItem);
	bindTaskEvents(listItem, taskComplete);

};
//edit an existing task
var editTask = function() {
	console.log('Edit Task...')
	var listItem = this.parentNode;
	var input = listItem.querySelector('input[type=text]');
	var label = listItem.querySelector('label');
	var editButton = listItem.querySelector("button.edit");
	//if the class of the parent is .editMode
	if(listItem.classList.contains("editMode")) {
		//label text become the input's value
		label.innerHTML = input.value;
		//save button changes back to edit button
		editButton.innerHTML = "Edit";
	} else {
		//input value becomes label's text
		input.value = label.innerHTML;
		//edit button changes to save button
		editButton.innerHTML = "Save";
	}
	//toggle .editMode
	listItem.classList.toggle("editMode");
};
//delete an existing task
var deleteTask = function() {
	console.log('Delete Task...')
		var listItem = this.parentNode;
		var ul = listItem.parentNode;
		//remove the parent list item from the ul
		ul.removeChild(listItem);
};
//mark a task as complete
var taskComplete = function() {
	//checkbox, when checked...
	console.log('Task Complete...')
		var listItem = this.parentNode;
		//append the task list item to the #completed-tasks
		completeTasksHolder.appendChild(listItem);
		bindTaskEvents(listItem, taskIncomplete);
};
//mark a task as incomplete
var taskIncomplete = function() {
	console.log('Task Incomplete...')
	//checkbox, when unchecked...
		var listItem = this.parentNode;
		//append the task list item to the #incomplete-tasks
		incompleteTasksHolder.appendChild(listItem);
		bindTaskEvents(listItem, taskComplete);
};

var bindTaskEvents = function(taskListItem, checkBoxEventHandler) {
		console.log("Bind list item events");
	//select listItem's children
	var checkBox = taskListItem.querySelector("input[type=checkBox]");
	var editButton = taskListItem.querySelector("button.edit");
	var deleteButton = taskListItem.querySelector("button.delete");
		//bind editTask to edit button
		editButton.onclick = editTask;
		//bind deleteTask to the  delete button
		deleteButton.onclick = deleteTask;
		//bind checkBoxEventHandler to the checkbox
		checkBox.onchange = checkBoxEventHandler;
		//check for open edits, change to save button
		if(editButton.parentNode.classList.contains("editMode")) {
			editButton.innerHTML = 'Save';
		}
}
var ajaxRequest = function() {
	console.log("AJAX Request");
}
//set the click handler to the addTask function
addButton.addEventListener("click", addTask);
addButton.addEventListener("click", ajaxRequest);
//cycle over incompleteTasksHolder ul list items
for(var i=0;i<incompleteTasksHolder.children.length; i++) {
	//bind events to list item's children (taskCompleted)
	bindTaskEvents(incompleteTasksHolder.children[i], taskComplete)
}

//cycle over completeTasksHolder ul list items
for(var i=0;i<completeTasksHolder.children.length; i++) {
	//bind events to list item's children(taskIncomplete)
	bindTaskEvents(completeTasksHolder.children[i], taskIncomplete)
}