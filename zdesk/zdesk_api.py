class ZendeskAPI:
    "Class generated from Zendesk REST API documentation. See api_gen.py."

    def __init__(self):
        pass

    def call(self, path, query=None, method='GET', status=200, data=None, **kwargs):
        pass

    # Duplicate API endpoint discarded: channels_voice_tickets_update from voice_integration
    # Duplicate API endpoint discarded: requests_search from requests
    # Duplicate API endpoint discarded: user_fields_reorder from user_fields
    # Duplicate API endpoint discarded: users_me from users
    # Duplicate API endpoint discarded: users_search from users


    def account_settings_create(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/account_settings"
        api_path = "/api/v2/account/settings.json"
        return self.call(api_path, "PUT", **kwargs)

    def account_settings_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/account_settings"
        api_path = "/api/v2/account/settings.json"
        return self.call(api_path, **kwargs)

    def activities_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/activity_stream"
        api_path = "/api/v2/activities.json"
        return self.call(api_path, **kwargs)

    def activity_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/activity_stream"
        api_path = "/api/v2/activities/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def app_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def app_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def app_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_installation_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def apps_installation_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def apps_installation_requirements(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations/{id}/requirements.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_installation_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_installations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations.json"
        return self.call(api_path, **kwargs)

    def apps_installations_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/installations.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def apps_job_status_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/job_statuses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_location_installation_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_location_installations"
        api_path = "/api/v2/apps/location_installations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_location_installations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_location_installations"
        api_path = "/api/v2/apps/location_installations.json"
        return self.call(api_path, **kwargs)

    def apps_location_installations_reorder(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_location_installations"
        api_path = "/api/v2/apps/location_installations/reorder.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def apps_location_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_locations"
        api_path = "/api/v2/apps/locations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def apps_locations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/app_locations"
        api_path = "/api/v2/apps/locations.json"
        return self.call(api_path, **kwargs)

    def apps_notify_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/notify.json"
        return self.call(api_path, "POST", data, **kwargs)

    def apps_owned_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/owned.json"
        return self.call(api_path, **kwargs)

    def apps_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps.json"
        return self.call(api_path, "POST", data, **kwargs)

    def apps_uploads_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/apps"
        api_path = "/api/v2/apps/uploads.json"
        return self.call(api_path, "POST", data, **kwargs)

    def attachment_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/attachments/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def attachment_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/attachments/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def audit_log_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/audit_logs"
        api_path = "/api/v2/audit_logs/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def audit_logs_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/audit_logs"
        api_path = "/api/v2/audit_logs.json"
        return self.call(api_path, **kwargs)

    def autocomplete_tags(self, name, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/autocomplete"
        api_path = "/api/v2/autocomplete/tags.json"
        api_query = {
            "name": name,
        }
        return self.call(api_path, api_query, **kwargs)

    def automation_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def automation_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def automation_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def automations_active_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations/active.json"
        return self.call(api_path, **kwargs)

    def automations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations.json"
        return self.call(api_path, **kwargs)

    def automations_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/automations"
        api_path = "/api/v2/automations.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def categories_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/categories.json"
        return self.call(api_path, **kwargs)

    def categories_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/categories.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def category_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/category/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def category_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/categories/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def category_forums(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/categories/{id}/forums.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def category_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/categories"
        api_path = "/api/v2/categories/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_twitter_monitored_twitter_handle_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/monitored_twitter_handles"
        api_path = "/api/v2/channels/twitter/monitored_twitter_handles/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_twitter_monitored_twitter_handles_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/monitored_twitter_handles"
        api_path = "/api/v2/channels/twitter/monitored_twitter_handles.json"
        return self.call(api_path, **kwargs)

    def channels_twitter_ticket_statuses(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/channels/twitter/tickets/{id}/statuses.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_twitter_tickets_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/channels/twitter/tickets.json"
        return self.call(api_path, "POST", data, **kwargs)

    def channels_voice_agent_ticket_display_update(self, agent_id, ticket_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice_integration"
        api_path = "/api/v2/channels/voice/agents/{agent_id}/tickets/{ticket_id}/display.json"
        api_path = api_path.format(agent_id=agent_id, ticket_id=ticket_id)
        return self.call(api_path, "POST", data, **kwargs)

    def channels_voice_agent_user_display_update(self, agent_id, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice_integration"
        api_path = "/api/v2/channels/voice/agents/{agent_id}/users/{user_id}/display.json"
        api_path = api_path.format(agent_id=agent_id, user_id=user_id)
        return self.call(api_path, "POST", data, **kwargs)

    def channels_voice_availability_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/availabilities/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def channels_voice_availability_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/availabilities/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_voice_greeting_categories_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/greeting_categories.json"
        return self.call(api_path, **kwargs)

    def channels_voice_greeting_category_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/greeting_category/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_voice_greeting_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/greetings/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def channels_voice_greeting_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/greetings/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def channels_voice_greeting_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/greetings/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_voice_greetings_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/greetings.json"
        return self.call(api_path, **kwargs)

    def channels_voice_greetings_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/greetings.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def channels_voice_phone_number_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/phone_numbers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def channels_voice_phone_number_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/phone_numbers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def channels_voice_phone_numbers_delete(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/phone_numbers.json"
        return self.call(api_path, "DELETE", **kwargs)

    def channels_voice_phone_numbers_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/phone_numbers.json"
        return self.call(api_path, **kwargs)

    def channels_voice_phone_numbers_search(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/phone_numbers/search.json"
        return self.call(api_path, **kwargs)

    def channels_voice_phone_numbers_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/phone_numbers.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def channels_voice_stats_agents_activity_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/stats/agents_activity.json"
        return self.call(api_path, **kwargs)

    def channels_voice_stats_current_queue_activity_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/stats/current_queue_activity.json"
        return self.call(api_path, **kwargs)

    def channels_voice_stats_historical_queue_activity_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice"
        api_path = "/api/v2/channels/voice/stats/historical_queue_activity.json"
        return self.call(api_path, **kwargs)

    def channels_voice_tickets_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/voice_integration"
        api_path = "/api/v2/channels/voice/tickets.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def custom_roles_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/custom_roles"
        api_path = "/api/v2/custom_roles.json"
        return self.call(api_path, **kwargs)

    def end_user_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/end_user"
        api_path = "/api/v2/end_users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def end_user_identities_update(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/end_users/{user_id}/identities.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, "POST", 201, data, **kwargs)

    def end_user_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/end_user"
        api_path = "/api/v2/end_users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def exports_tickets(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_export"
        api_path = "/api/v2/exports/tickets.json"
        return self.call(api_path, **kwargs)

    def exports_tickets_sample(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_export"
        api_path = "/api/v2/exports/tickets/sample.json"
        return self.call(api_path, **kwargs)

    def forum_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def forum_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def forum_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def forum_subscription_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forum_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def forum_subscription_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forum_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def forum_subscriptions(self, forum_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forums/{forum_id}/subscriptions.json"
        api_path = api_path.format(forum_id=forum_id)
        return self.call(api_path, **kwargs)

    def forum_subscriptions_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forum_subscriptions.json"
        return self.call(api_path, **kwargs)

    def forum_subscriptions_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/forum_subscriptions.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def forum_topics(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/forums/{id}/topics.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def forums_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums.json"
        return self.call(api_path, **kwargs)

    def forums_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forums"
        api_path = "/api/v2/forums.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def group_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def group_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def group_membership_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def group_membership_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def group_memberships(self, group_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/groups/{group_id}/memberships.json"
        api_path = api_path.format(group_id=group_id)
        return self.call(api_path, **kwargs)

    def group_memberships_assignable(self, group_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/groups/{group_id}/memberships/assignable.json"
        api_path = api_path.format(group_id=group_id)
        return self.call(api_path, **kwargs)

    def group_memberships_assignable_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships/assignable.json"
        return self.call(api_path, **kwargs)

    def group_memberships_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships.json"
        return self.call(api_path, **kwargs)

    def group_memberships_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/group_memberships.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def group_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def group_users(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/groups/{id}/users.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def groups_assignable_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups/assignable.json"
        return self.call(api_path, **kwargs)

    def groups_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups.json"
        return self.call(api_path, **kwargs)

    def groups_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/groups.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def import_topic_comments(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/import/topics/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "POST", data, **kwargs)

    def import_topics(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/import/topics.json"
        return self.call(api_path, "POST", data, **kwargs)

    def imports_tickets(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_import"
        api_path = "/api/v2/imports/tickets.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def job_status_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/job_statuses"
        api_path = "/api/v2/job_statuses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def locale_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def locales_agent_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales/agent.json"
        return self.call(api_path, **kwargs)

    def locales_current_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales/current.json"
        return self.call(api_path, **kwargs)

    def locales_detect_best_locale(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales/detect_best_locale.json"
        return self.call(api_path, **kwargs)

    def locales_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/locales"
        api_path = "/api/v2/locales.json"
        return self.call(api_path, **kwargs)

    def macro_apply(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/{id}/apply.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def macro_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def macro_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def macro_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def macros_active_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros/active.json"
        return self.call(api_path, **kwargs)

    def macros_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros.json"
        return self.call(api_path, **kwargs)

    def macros_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/macros.json"
        return self.call(api_path, "POST", data, **kwargs)

    def oauth_client_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def oauth_client_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def oauth_client_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def oauth_clients_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients.json"
        return self.call(api_path, **kwargs)

    def oauth_clients_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/oauth/clients.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def oauth_token_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_tokens"
        api_path = "/api/v2/oauth/tokens/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def oauth_token_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_tokens"
        api_path = "/api/v2/oauth/tokens/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def oauth_tokens_current_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_tokens"
        api_path = "/api/v2/oauth/tokens/current.json"
        return self.call(api_path, **kwargs)

    def oauth_tokens_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_tokens"
        api_path = "/api/v2/oauth/tokens.json"
        return self.call(api_path, **kwargs)

    def organization_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def organization_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def organization_field_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def organization_field_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def organization_field_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_fields_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields.json"
        return self.call(api_path, **kwargs)

    def organization_fields_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/organization_fields.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def organization_related(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/{id}/related.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_requests(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/organizations/{id}/requests.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_tags(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/organizations/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_tags_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/organizations/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def organization_tags_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/organizations/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def organization_tags_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/organizations/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "POST", data, **kwargs)

    def organization_tickets(self, organization_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/organizations/{organization_id}/tickets.json"
        api_path = api_path.format(organization_id=organization_id)
        return self.call(api_path, **kwargs)

    def organization_users(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/organizations/{id}/users.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organizations_autocomplete(self, name, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/autocomplete.json"
        api_query = {
            "name": name,
        }
        return self.call(api_path, api_query, **kwargs)

    def organizations_create_many(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/create_many.json"
        return self.call(api_path, "POST", data, **kwargs)

    def organizations_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations.json"
        return self.call(api_path, **kwargs)

    def organizations_search(self, external_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations/search.json"
        api_query = {
            "external_id": external_id,
        }
        return self.call(api_path, api_query, **kwargs)

    def organizations_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/organizations.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def portal_search(self, query, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/search"
        api_path = "/api/v2/portal/search.json"
        api_query = {
            "query": query,
        }
        return self.call(api_path, api_query, **kwargs)

    def problems_autocomplete(self, text, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/problems/autocomplete.json"
        api_query = {
            "text": text,
        }
        return self.call(api_path, api_query, "POST", data, **kwargs)

    def problems_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/problems.json"
        return self.call(api_path, **kwargs)

    def recipient_address_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def recipient_address_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def recipient_address_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def recipient_address_verify(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses/{id}/verify.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def recipient_addresses_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses.json"
        return self.call(api_path, **kwargs)

    def recipient_addresses_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/support_addresses"
        api_path = "/api/v2/recipient_addresses.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def request_comment_show(self, request_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/{request_id}/comments/{id}.json"
        api_path = api_path.format(request_id=request_id, id=id)
        return self.call(api_path, **kwargs)

    def request_comments(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def request_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def request_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def requests(self, status, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests.json"
        api_query = {
            "status": status,
        }
        return self.call(api_path, api_query, **kwargs)

    def requests_ccd_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/ccd.json"
        return self.call(api_path, **kwargs)

    def requests_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests.json"
        return self.call(api_path, **kwargs)

    def requests_open_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/open.json"
        return self.call(api_path, **kwargs)

    def requests_search(self, query, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/search.json"
        api_query = {
            "query": query,
        }
        return self.call(api_path, api_query, **kwargs)

    def requests_solved_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests/solved.json"
        return self.call(api_path, **kwargs)

    def requests_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/requests.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def satisfaction_rating_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/satisfaction_ratings"
        api_path = "/api/v2/satisfaction_ratings/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def satisfaction_ratings_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/satisfaction_ratings"
        api_path = "/api/v2/satisfaction_ratings.json"
        return self.call(api_path, **kwargs)

    def search(self, query, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/search"
        api_path = "/api/v2/search.json"
        api_query = {
            "query": query,
        }
        return self.call(api_path, api_query, **kwargs)

    def sharing_agreements_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/sharing_agreements"
        api_path = "/api/v2/sharing_agreements.json"
        return self.call(api_path, **kwargs)

    def suspended_ticket_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def suspended_ticket_recover(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/{id}/recover.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def suspended_ticket_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def suspended_tickets_destroy_many(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/destroy_many.json"
        api_query = {
            "ids": ids,
        }
        return self.call(api_path, api_query, "DELETE", **kwargs)

    def suspended_tickets_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets.json"
        return self.call(api_path, **kwargs)

    def suspended_tickets_recover_many(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/suspended_tickets"
        api_path = "/api/v2/suspended_tickets/recover_many.json"
        api_query = {
            "ids": ids,
        }
        return self.call(api_path, api_query, "PUT", **kwargs)

    def tags_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tags.json"
        return self.call(api_path, **kwargs)

    def target_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def target_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def target_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def targets_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets.json"
        return self.call(api_path, **kwargs)

    def targets_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/targets"
        api_path = "/api/v2/targets.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def ticket_audit_make_private(self, ticket_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_audits"
        api_path = "/api/v2/tickets/{ticket_id}/audits/{id}/make_private.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, "PUT", **kwargs)

    def ticket_audit_show(self, ticket_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_audits"
        api_path = "/api/v2/tickets/{ticket_id}/audits/{id}.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, **kwargs)

    def ticket_audits(self, ticket_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_audits"
        api_path = "/api/v2/tickets/{ticket_id}/audits.json"
        api_path = api_path.format(ticket_id=ticket_id)
        return self.call(api_path, **kwargs)

    def ticket_collaborators(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/collaborators.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_comment_attachment_redact(self, ticket_id, comment_id, attachment_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/tickets/{ticket_id}/comments/{comment_id}/attachments/{attachment_id}/redact.json"
        api_path = api_path.format(ticket_id=ticket_id, comment_id=comment_id, attachment_id=attachment_id)
        return self.call(api_path, "PUT", **kwargs)

    def ticket_comment_make_private(self, ticket_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_comments"
        api_path = "/api/v2/tickets/{ticket_id}/comments/{id}/make_private.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, "PUT", **kwargs)

    def ticket_comment_redact(self, ticket_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_comments"
        api_path = "/api/v2/tickets/{ticket_id}/comments/{id}/redact.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, "PUT", **kwargs)

    def ticket_comments(self, ticket_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_comments"
        api_path = "/api/v2/tickets/{ticket_id}/comments.json"
        api_path = api_path.format(ticket_id=ticket_id)
        return self.call(api_path, **kwargs)

    def ticket_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def ticket_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def ticket_field_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def ticket_field_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def ticket_field_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_fields_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields.json"
        return self.call(api_path, **kwargs)

    def ticket_fields_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_fields"
        api_path = "/api/v2/ticket_fields.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def ticket_form_clone(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/{id}/clone.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "POST", 201, data, **kwargs)

    def ticket_form_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def ticket_form_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def ticket_form_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_forms_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms.json"
        return self.call(api_path, **kwargs)

    def ticket_forms_reorder(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms/reorder.json"
        return self.call(api_path, "PUT", **kwargs)

    def ticket_forms_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_forms"
        api_path = "/api/v2/ticket_forms.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def ticket_incidents(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/incidents.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_macro_apply(self, ticket_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/macros"
        api_path = "/api/v2/tickets/{ticket_id}/macros/{id}/apply.json"
        api_path = api_path.format(ticket_id=ticket_id, id=id)
        return self.call(api_path, **kwargs)

    def ticket_mark_as_spam(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/mark_as_spam.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def ticket_merge(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/merge.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "POST", data, **kwargs)

    def ticket_metric_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_metrics"
        api_path = "/api/v2/ticket_metrics/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_metrics(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_metrics"
        api_path = "/api/v2/tickets/{id}/metrics.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_metrics_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/ticket_metrics"
        api_path = "/api/v2/ticket_metrics.json"
        return self.call(api_path, **kwargs)

    def ticket_related(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}/related.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_satisfaction_rating_update(self, ticket_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/satisfaction_ratings"
        api_path = "/api/v2/tickets/{ticket_id}/satisfaction_rating.json"
        api_path = api_path.format(ticket_id=ticket_id)
        return self.call(api_path, "POST", data, **kwargs)

    def ticket_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_tags(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tickets/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def ticket_tags_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tickets/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def ticket_tags_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tickets/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def ticket_tags_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/tickets/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "POST", data, **kwargs)

    def tickets_destroy_many(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/destroy_many.json"
        api_query = {
            "ids": ids,
        }
        return self.call(api_path, api_query, "DELETE", **kwargs)

    def tickets_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets.json"
        return self.call(api_path, **kwargs)

    def tickets_mark_many_as_spam(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/mark_many_as_spam.json"
        api_query = {
            "ids": ids,
        }
        return self.call(api_path, api_query, "PUT", **kwargs)

    def tickets_recent_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/recent.json"
        return self.call(api_path, **kwargs)

    def tickets_show_many(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/show_many.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def tickets_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def tickets_update_many_create(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/tickets/update_many.json"
        api_query = {
            "ids": ids,
        }
        return self.call(api_path, api_query, "PUT", **kwargs)

    def topic_comment_create(self, topic_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{topic_id}/comments/{id}.json"
        api_path = api_path.format(topic_id=topic_id, id=id)
        return self.call(api_path, "PUT", **kwargs)

    def topic_comment_delete(self, topic_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{topic_id}/comments/{id}.json"
        api_path = api_path.format(topic_id=topic_id, id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def topic_comment_show(self, topic_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{topic_id}/comments/{id}.json"
        api_path = api_path.format(topic_id=topic_id, id=id)
        return self.call(api_path, **kwargs)

    def topic_comments(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topic_comments_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/topics/{id}/comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "POST", 201, data, **kwargs)

    def topic_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def topic_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def topic_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topic_subscription_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topic_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def topic_subscription_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topic_subscriptions/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topic_subscriptions(self, topic_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topics/{topic_id}/subscriptions.json"
        api_path = api_path.format(topic_id=topic_id)
        return self.call(api_path, **kwargs)

    def topic_subscriptions_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topic_subscriptions.json"
        return self.call(api_path, **kwargs)

    def topic_subscriptions_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/topic_subscriptions.json"
        return self.call(api_path, "POST", data, **kwargs)

    def topic_tags(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/topics/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topic_tags_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/topics/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def topic_tags_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/topics/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def topic_tags_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tags"
        api_path = "/api/v2/topics/{id}/tags.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "POST", data, **kwargs)

    def topic_vote(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/topics/{id}/vote.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, 404, **kwargs)

    def topic_vote_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/topics/{id}/vote.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def topic_vote_update(self, id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/topics/{id}/vote.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "POST", 201, data, **kwargs)

    def topic_votes(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/topics/{id}/votes.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def topics_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics.json"
        return self.call(api_path, **kwargs)

    def topics_show_many(self, ids, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics/show_many.json"
        api_query = {
            "ids": ids,
        }
        return self.call(api_path, api_query, "POST", data, **kwargs)

    def topics_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/topics.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def trigger_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def trigger_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def trigger_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def triggers_active_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/active.json"
        return self.call(api_path, **kwargs)

    def triggers_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers.json"
        return self.call(api_path, **kwargs)

    def triggers_reorder(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers/reorder.json"
        return self.call(api_path, "PUT", **kwargs)

    def triggers_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/triggers"
        api_path = "/api/v2/triggers.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def upload_delete(self, token, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/uploads/{token}.json"
        api_path = api_path.format(token=token)
        return self.call(api_path, "DELETE", **kwargs)

    def uploads_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/attachments"
        api_path = "/api/v2/uploads.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def user_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def user_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def user_field_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def user_field_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def user_field_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_fields_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields.json"
        return self.call(api_path, **kwargs)

    def user_fields_reorder(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organization_fields"
        api_path = "/api/v2/user_fields/reorder.json"
        return self.call(api_path, "PUT", **kwargs)

    def user_fields_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_fields"
        api_path = "/api/v2/user_fields.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def user_forum_subscriptions(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/forum_subscriptions"
        api_path = "/api/v2/users/{user_id}/forum_subscriptions.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_group_membership_delete(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def user_group_membership_make_default(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships/{id}/make_default.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, "PUT", **kwargs)

    def user_group_membership_show(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, **kwargs)

    def user_group_memberships(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_group_memberships_update(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/group_memberships"
        api_path = "/api/v2/users/{user_id}/group_memberships.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, "POST", 201, data, **kwargs)

    def user_groups(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/groups"
        api_path = "/api/v2/users/{user_id}/groups.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_identities(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_identities_update(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, "POST", 201, data, **kwargs)

    def user_identity_create(self, user_id, id, identity_verified, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        api_query = {
            "identity[verified]": identity_verified,
        }
        return self.call(api_path, api_query, "PUT", **kwargs)

    def user_identity_delete(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def user_identity_make_primary(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}/make_primary"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, "PUT", **kwargs)

    def user_identity_show(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, **kwargs)

    def user_identity_verify(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/user_identities"
        api_path = "/api/v2/users/{user_id}/identities/{id}/verify"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, "PUT", **kwargs)

    def user_merge(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{user_id}/merge.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, "PUT", **kwargs)

    def user_organizations(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/organizations"
        api_path = "/api/v2/users/{user_id}/organizations.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_password_create(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{user_id}/password.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, "PUT", **kwargs)

    def user_password_update(self, user_id, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{user_id}/password.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, "POST", data, **kwargs)

    def user_related(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{id}/related.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_requests(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/requests"
        api_path = "/api/v2/users/{id}/requests.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_tickets_ccd(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/users/{user_id}/tickets/ccd.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_tickets_requested(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/tickets"
        api_path = "/api/v2/users/{user_id}/tickets/requested.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_topic_comment_show(self, user_id, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/users/{user_id}/topic_comments/{id}.json"
        api_path = api_path.format(user_id=user_id, id=id)
        return self.call(api_path, **kwargs)

    def user_topic_comments(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_comments"
        api_path = "/api/v2/users/{id}/topic_comments.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_topic_subscriptions(self, user_id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_subscriptions"
        api_path = "/api/v2/users/{user_id}/topic_subscriptions.json"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def user_topic_votes(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topic_votes"
        api_path = "/api/v2/users/{id}/topic_votes.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def user_topics(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/topics"
        api_path = "/api/v2/users/{id}/topics.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def users_autocomplete(self, name, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/autocomplete.json"
        api_query = {
            "name": name,
        }
        return self.call(api_path, api_query, **kwargs)

    def users_create_many(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/create_many.json"
        return self.call(api_path, "POST", data, **kwargs)

    def users_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users.json"
        return self.call(api_path, **kwargs)

    def users_me(self, include, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/side_loading"
        api_path = "/api/v2/users/me.json"
        api_query = {
            "include": include,
        }
        return self.call(api_path, api_query, **kwargs)

    def users_me_merge(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/me/merge.json"
        return self.call(api_path, "PUT", **kwargs)

    def users_me_oauth_clients(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/oauth_clients"
        api_path = "/api/v2/users/me/oauth/clients.json"
        return self.call(api_path, **kwargs)

    def users_search(self, query, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/search.json"
        api_query = {
            "query": query,
        }
        return self.call(api_path, api_query, **kwargs)

    def users_show_many(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users/show_many.json"
        api_query = {
            "ids": ids,
        }
        return self.call(api_path, api_query, **kwargs)

    def users_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/users"
        api_path = "/api/v2/users.json"
        return self.call(api_path, "POST", 201, data, **kwargs)

    def view_count(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}/count.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def view_create(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "PUT", **kwargs)

    def view_delete(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, "DELETE", **kwargs)

    def view_execute(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}/execute.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def view_export(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}/export.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def view_show(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def view_tickets(self, id, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/{id}/tickets.json"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def views_active_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/active.json"
        return self.call(api_path, **kwargs)

    def views_compact(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/compact.json"
        return self.call(api_path, **kwargs)

    def views_count_many(self, ids, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/count_many.json"
        api_query = {
            "ids": ids,
        }
        return self.call(api_path, api_query, **kwargs)

    def views_list(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views.json"
        return self.call(api_path, **kwargs)

    def views_preview(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/preview.json"
        return self.call(api_path, "POST", data, **kwargs)

    def views_preview_count(self, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views/preview/count.json"
        return self.call(api_path, **kwargs)

    def views_update(self, data, **kwargs):
        "http://developer.zendesk.com/rest_api/docs/core/views"
        api_path = "/api/v2/views.json"
        return self.call(api_path, "POST", 201, data, **kwargs)



