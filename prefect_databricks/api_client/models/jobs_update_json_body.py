from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..models.job_settings import JobSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsUpdateJsonBody")


class JobsUpdateJsonBody(BaseModel):
    """
    Attributes:
        job_id (int): The canonical identifier of the job to update. This field is required. Example: 11223344.
        fields_to_remove (Union[Unset, List[str]]): Remove top-level fields in the job settings. Removing nested fields
            is not supported. This field is optional. Example: ['libraries', 'schedule'].
        new_settings (Union[Unset, JobSettings]):
    """

    job_id: int = None
    fields_to_remove: Union[Unset, List[str]] = UNSET
    new_settings: Union[Unset, JobSettings] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        fields_to_remove: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fields_to_remove, Unset):
            fields_to_remove = self.fields_to_remove

        new_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_settings, Unset):
            new_settings = self.new_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
            }
        )
        if fields_to_remove is not UNSET:
            field_dict["fields_to_remove"] = fields_to_remove
        if new_settings is not UNSET:
            field_dict["new_settings"] = new_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        job_id = d.pop("job_id")

        fields_to_remove = cast(List[str], d.pop("fields_to_remove", UNSET))

        _new_settings = d.pop("new_settings", UNSET)
        new_settings: Union[Unset, JobSettings]
        if isinstance(_new_settings, Unset):
            new_settings = UNSET
        else:
            new_settings = JobSettings.from_dict(_new_settings)

        jobs_update_json_body = cls(
            job_id=job_id,
            fields_to_remove=fields_to_remove,
            new_settings=new_settings,
        )

        jobs_update_json_body.additional_properties = d
        return jobs_update_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties