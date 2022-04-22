package ${PACKAGE}.mapper;

import com.uda.examples.model.${SINGLE_ROUTE_NAME_CAPITALIZE};
import com.uda.examples.entity.${SINGLE_ROUTE_NAME_CAPITALIZE}Entity;
import org.springframework.stereotype.Component;

@Component
public class ${SINGLE_ROUTE_NAME_CAPITALIZE}Mapper {

    public ${SINGLE_ROUTE_NAME_CAPITALIZE} map(${SINGLE_ROUTE_NAME_CAPITALIZE}Entity ${SINGLE_ROUTE_NAME}Entity) {
        return ${SINGLE_ROUTE_NAME_CAPITALIZE}.builder()
                ${MAPPER_BODY_ENTITY}
                .build();
    }

    public ${SINGLE_ROUTE_NAME_CAPITALIZE}Entity map(${SINGLE_ROUTE_NAME_CAPITALIZE} ${SINGLE_ROUTE_NAME}) {
        return ${SINGLE_ROUTE_NAME_CAPITALIZE}Entity.builder()
                ${MAPPER_BODY_MODEL}
                .build();
    }
}
