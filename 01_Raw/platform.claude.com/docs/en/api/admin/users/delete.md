---
source_url: https://platform.claude.com/docs/en/api/admin/users/delete
fetched_at: 2026-08-31T06:29:43.558829+00:00
fetch_method: mintlify_md
---

# Remove User

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

## Path parameters

- `user_id: string`

  ID of the User.

## Returns

- `id: string`

  ID of the User.

- `type: "user_deleted"`

  Deleted object type.

  For Users, this is always `"user_deleted"`.

  default: user_deleted

## Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```
