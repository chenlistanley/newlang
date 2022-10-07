
def test()
	a = {"A"=>"apple", "B"=>"banana"}
	for k,v in a
		puts "#{k} #{v}"
	end
end

def test()
	a = {"A" => "apple", "B" => "banana"}
	a.store("C", "orange")
	a.each{|k, v| puts "#{k} #{v}"}
end

