from django.db import models

class Page(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()

	parent = models.ForeignKey('self', null=True, blank=True)

	def history(self):
		output = []
		current = self.parent
		while current is not None:
			output.append(current)
			current = current.parent 
		return output


	def __unicode__(self):
		return "%d - %s" % (self.id, self.title)

	def get_absolute_url(self):
		return "/%d/" % self.id