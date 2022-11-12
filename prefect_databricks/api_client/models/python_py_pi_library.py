from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PythonPyPiLibrary")


class PythonPyPiLibrary(BaseModel):
    """
    Attributes:
        package (str): The name of the PyPI package to install. An optional exact version specification is also
            supported. Examples: `simplejson` and `simplejson==3.8.0`. This field is required. Example: simplejson==3.8.0.
        repo (Union[Unset, str]): The repository where the package can be found. If not specified, the default pip index
            is used. Example: https://my-repo.com.
    """

    package: str = None
    repo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package = self.package
        repo = self.repo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package": package,
            }
        )
        if repo is not UNSET:
            field_dict["repo"] = repo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        package = d.pop("package")

        repo = d.pop("repo", UNSET)

        python_py_pi_library = cls(
            package=package,
            repo=repo,
        )

        python_py_pi_library.additional_properties = d
        return python_py_pi_library

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