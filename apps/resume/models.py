from django.db import models


class ResumeItem(models.Model):
    """
    A single resume item, representing a job and title held over a given period
    of time.
    """
    user = models.ForeignKey('auth.User') # left as a security measure 

    resume = models.ForeignKey('Resume',
        on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=127)
    company = models.CharField(max_length=127)

    start_date = models.DateField()
    # Null end date indicates position is currently held
    end_date = models.DateField(null=True, blank=True)

    description = models.TextField(max_length=2047, blank=True)

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.user.username,
                                          self.title,
                                          self.company,
                                          self.start_date.isoformat())

class Resume(models.Model): 
    """
    A single resume, holding all resume items for a resume. 
    """

    user = models.ForeignKey('auth.User')

    title = models.CharField(max_length=127, default='Default Resume')    
    description = models.TextField(max_length=2047, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)