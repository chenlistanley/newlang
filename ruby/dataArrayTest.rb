def test()
	a = ["apple", "banana"]
	for k in a
		puts "#{k}"
	end
end

def test()
	a = ["apple", "banana"]
	a.append("orange")
	a.each{|k| puts "#{k}"}
end

