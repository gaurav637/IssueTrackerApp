# from zango.db import models
# from zango.contrib.auth.models import AppUserModel

# class Issue(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     status = models.CharField(
#         max_length=20,
#         choices=[
#             ('Open', 'Open'),
#             ('In Progress', 'In Progress'),
#             ('Resolved', 'Resolved')
#         ],
#         default='Open'
#     )
#     assignee = models.ForeignKey(
#         AppUserModel,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name='assigned_issues'
#     )
#     created_by = models.ForeignKey(
#         AppUserModel,
#         on_delete=models.CASCADE,
#         related_name='created_issues'
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-created_at']