SELECT ps.id, ps.name, ps.chile_atiende_id 
FROM public_services_publicservice AS ps 
WHERE ps.id NOT IN (
	SELECT pubs.id 
	FROM public_services_publicservice AS pubs, 
	companies_company AS c, 
	projects_project as p, 
	permit_requests_permitrequest AS pr, 
	permits_permit as per 
	WHERE c.name = 'MORGAN SA' 
	and c.id = p.company_id 
	AND p.id = pr.project_id 
	AND per.id = pr.permit_id 
	AND per.public_service_id = pubs.id
);
