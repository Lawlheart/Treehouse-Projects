require './todo_item'

class TodoList
  attr_reader :name, :todo_items

  def initialize(name)
    @name = name
    @todo_items = []
  end

  def add_item(name)
    @todo_items.push(TodoItem.new(name))
  end

  def find_index(name)
    @todo_items.each_with_index do |todo_item, index|
      return index if (todo_item.name == name)
    end
    nil
  end

  def remove_item(name)
    index = find_index(name)
    @todo_items.delete_at(index) if index
    !index.nil?
  end

  def mark_complete(name)
    index = find_index(name)
    @todo_items[index].mark_complete! if index
    !index.nil?
  end

  def print_list(kind = 'all')
    puts "#{name} List - #{kind} items"
    puts "-"*30
    todo_items.each do |todo_item|
      case kind
        when 'complete'
          puts todo_item if todo_item.complete?
        when 'incomplete'
          puts todo_item unless todo_item.complete?
      else
        puts todo_item
      end
    end
    puts "\n"
  end
end

todo_list = TodoList.new("groceries")
todo_list.add_item("milk")
todo_list.add_item("eggs")
todo_list.add_item("bread")
todo_list.add_item("butter")

todo_list.mark_complete("milk")

todo_list.print_list
todo_list.print_list('complete')
todo_list.print_list('incomplete')