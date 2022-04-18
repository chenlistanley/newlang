
function test()
	a = {"apple", "banana"}
	for i=1,2 do
		print(a[i])
	end
end


function test()
	a = {"apple", "banana"}
	for _,v in ipairs(a) do
		print(v)
	end
end
