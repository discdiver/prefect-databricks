from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsRunsSubmitResponse200")


class JobsRunsSubmitResponse200(BaseModel):
    """
    Attributes:
        run_id (Union[Unset, int]): The canonical identifier for the newly submitted run. Example: 455644833.
    """

    run_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_id = self.run_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["run_id"] = run_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        run_id = d.pop("run_id", UNSET)

        jobs_runs_submit_response_200 = cls(
            run_id=run_id,
        )

        jobs_runs_submit_response_200.additional_properties = d
        return jobs_runs_submit_response_200

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