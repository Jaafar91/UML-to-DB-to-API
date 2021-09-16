package ${PACKAGE}.model;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Builder
@Setter
@Getter
public class ${SINGLE_ROUTE_NAME_CAPITALIZE}Data {
    private List<${SINGLE_ROUTE_NAME_CAPITALIZE}> ${SINGLE_ROUTE_NAME};
}
