class Name
  attr_accessor :title, :first, :middle, :last, :suffix

  def initialize(title, first, middle, last, suffix)
    @title = title
    @first = first
    @middle = middle
    @last = last
    @suffix = suffix
  end


  def full
    "#{@first} #{@middle} #{@last} #{@suffix}"
  end

  def full_with_title
    "#{@title} #{full}"
  end


  def to_s
    if @title.empty?
      full
    else
      full_with_title
    end
  end

end