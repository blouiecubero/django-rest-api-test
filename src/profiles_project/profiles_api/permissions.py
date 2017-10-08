# -*- coding: utf-8 -*-
# @Author: newuser
# @Date:   2017-10-08 08:34:14
# @Last Modified by:   newuser
# @Last Modified time: 2017-10-08 10:06:50

from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		if request.method in permissions.SAFE_METHODS:
			return True


		return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.user_profile.id == request.user.id