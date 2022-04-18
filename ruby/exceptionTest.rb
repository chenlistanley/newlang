
def test()
	begin
		raise "apple error"
	rescue Exception => e
		puts "error #{e}"
	ensure
		puts "banana"
	end
end