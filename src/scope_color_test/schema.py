from pydantic import Field

from scope.core.pipelines.base_schema import BasePipelineConfig, ModeDefaults, ui_field_config


class ColorTestConfig(BasePipelineConfig):
    """Configuration for the Color Test pipeline."""

    pipeline_id = "color-test"
    pipeline_name = "Color Test"
    pipeline_description = "Blends a solid color with input video using RGBA controls"

    supports_prompts = False

    modes = {"video": ModeDefaults(default=True)}

    # --- Color Controls ---

    red: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Red channel value (0.0 = none, 1.0 = maximum)",
        json_schema_extra=ui_field_config(order=1, label="Red"),
    )

    green: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Green channel value (0.0 = none, 1.0 = maximum)",
        json_schema_extra=ui_field_config(order=2, label="Green"),
    )

    blue: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Blue channel value (0.0 = none, 1.0 = maximum)",
        json_schema_extra=ui_field_config(order=3, label="Blue"),
    )

    alpha: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Blend amount (0.0 = original video, 1.0 = full color)",
        json_schema_extra=ui_field_config(order=4, label="Alpha"),
    )
