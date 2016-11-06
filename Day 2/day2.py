class Present():
	def __init__(self, len, wid, hght):
		self.l = int(len)
		self.w = int(wid)
		self.h = int(hght)
		self.area = 0
		self.slack = 0
		self.dimensions = [self.l, self.w, self.h]
		self.dimensions.sort()


	def surface_area(self):
		self.area = (2 * self.l * self.w) + (2 * self.w * self.h) + (2 * self.h * self.l)
		return self.area

	def slack_area(self):
		self.slack =  self.dimensions[0] * self.dimensions[1]
		return self.slack

	def ribbon_length(self):
		self.ribbon = (self.l * self.w * self.h) + (2 * (self.dimensions[0] + self.dimensions[1]) )
		return self.ribbon



def main():
	total_paper = 0
	total_ribbon = 0
	with open("input2", "r") as f:
		 lines = f.readlines()
	for line in lines:
		dimensions = line.split("x")
		p =  Present(dimensions[0], dimensions[1], dimensions[2])
		total_paper += p.surface_area() + p.slack_area()
		total_ribbon += p.ribbon_length()
	print "Total Paper: " + total_paper
	print "Totak Ribbon:" + total_ribbon

if __name__ == "__main__" : main()