from fastapi import Depends, HTTPException, status
from oauth2 import get_current_user


def admin_only(current_user=Depends(get_current_user)):
    if current_user["role"] != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Admin can perform this action."
        )
    return current_user


def admin_or_store_manager(current_user=Depends(get_current_user)):
    if current_user["role"] not in ["Admin", "Store Manager"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access Denied."
        )
    return current_user